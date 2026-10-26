"""Tests for analyze_supply_chain.py: data validation, KPI maths, reorder logic and documentation."""

import pandas as pd
import pytest

from conftest import COMMITTED_OUTPUTS, README_PATH

EXPECTED_CSVS = [
    "kpi_summary.csv",
    "category_summary.csv",
    "monthly_sales.csv",
    "region_summary.csv",
    "warehouse_summary.csv",
    "inventory_reorder_alerts.csv",
]
EXPECTED_CHARTS = ["sales_by_category.png", "monthly_sales_trend.png"]


def make_rows(**overrides):
    """Two valid order rows, with any column overridden for both rows."""
    base = {
        "order_id": ["ORD-1", "ORD-2"],
        "order_date": ["2025-01-05", "2025-02-10"],
        "region": ["North", "South"],
        "warehouse": ["Pune", "Pune"],
        "category": ["Electronics", "Industrial"],
        "sku": ["EL-1", "IN-1"],
        "quantity": [10, 5],
        "unit_price": [20.0, 40.0],
        "unit_cost": [12.0, 25.0],
        "lead_time_days": [5, 7],
        "stock_on_hand": [100, 100],
        "reorder_point": [10, 10],
    }
    base.update(overrides)
    return pd.DataFrame(base)


# --- The committed dataset ---------------------------------------------------


def test_source_data_has_required_columns_and_unique_orders(module, source_data):
    assert module.REQUIRED.issubset(source_data.columns)
    assert not source_data["order_id"].duplicated().any()


def test_source_data_has_no_negative_numbers(module, source_data):
    assert (source_data[module.NUMERIC_COLUMNS] >= 0).all().all()


# --- A full run on the committed dataset --------------------------------------


@pytest.fixture
def full_run(run_analysis, source_data):
    return run_analysis(source_data)


def test_run_creates_every_expected_file(full_run):
    for name in EXPECTED_CSVS + EXPECTED_CHARTS:
        path = full_run / name
        assert path.is_file(), f"missing output: {name}"
        assert path.stat().st_size > 0, f"empty output: {name}"


def test_kpis_match_the_documented_snapshot(full_run):
    kpis = pd.read_csv(full_run / "kpi_summary.csv").set_index("metric")["value"]
    assert kpis["order_count"] == 120
    assert kpis["total_units"] == 1620
    assert kpis["unique_skus"] == 20
    assert kpis["total_sales"] == pytest.approx(140275.80, abs=0.01)
    assert kpis["estimated_cost"] == pytest.approx(87500.24, abs=0.01)
    assert kpis["estimated_gross_profit"] == pytest.approx(52775.56, abs=0.01)
    assert kpis["estimated_gross_margin_pct"] == pytest.approx(37.62, abs=0.01)


def test_project_readme_states_the_same_kpis():
    text = README_PATH.read_text(encoding="utf-8")
    for expected in ["1,620", "140,275.80", "87,500.24", "52,775.56", "37.62%"]:
        assert expected in text, f"README no longer mentions {expected}; update it or the data"


@pytest.mark.parametrize("name", EXPECTED_CSVS)
def test_committed_output_snapshots_are_current(full_run, name):
    # The committed CSVs are rounded for display, so compare numbers with a small tolerance.
    regenerated = pd.read_csv(full_run / name)
    committed = pd.read_csv(COMMITTED_OUTPUTS / name)
    pd.testing.assert_frame_equal(regenerated, committed, check_dtype=False, atol=0.01, rtol=0)


def test_category_totals_add_up_to_the_kpis(full_run):
    kpis = pd.read_csv(full_run / "kpi_summary.csv").set_index("metric")["value"]
    category = pd.read_csv(full_run / "category_summary.csv")
    assert category["sales"].sum() == pytest.approx(kpis["total_sales"], abs=0.01)
    assert category["estimated_gross_profit"].sum() == pytest.approx(
        kpis["estimated_gross_profit"], abs=0.01
    )


# --- Calculations on a small, hand-checkable dataset -------------------------


def test_sales_cost_profit_and_margin_on_small_input(run_analysis):
    out = run_analysis(make_rows())
    kpis = pd.read_csv(out / "kpi_summary.csv").set_index("metric")["value"]
    # Sales: 10*20 + 5*40 = 400. Cost: 10*12 + 5*25 = 245. Profit: 155.
    assert kpis["total_sales"] == pytest.approx(400.0)
    assert kpis["estimated_cost"] == pytest.approx(245.0)
    assert kpis["estimated_gross_profit"] == pytest.approx(155.0)
    assert kpis["estimated_gross_margin_pct"] == pytest.approx(38.75)
    assert kpis["total_units"] == 15


def test_reorder_alert_when_latest_stock_is_at_or_below_reorder_point(run_analysis):
    frame = make_rows(
        order_id=["ORD-1", "ORD-2"],
        order_date=["2025-01-05", "2025-02-10"],
        warehouse=["Pune", "Pune"],
        category=["Electronics", "Electronics"],
        sku=["EL-1", "EL-1"],
        stock_on_hand=[100, 10],  # the latest row has stock equal to the reorder point
        reorder_point=[10, 10],
    )
    alerts = pd.read_csv(run_analysis(frame) / "inventory_reorder_alerts.csv")
    assert alerts["sku"].tolist() == ["EL-1"]


def test_no_reorder_alert_when_only_an_older_row_was_low(run_analysis):
    frame = make_rows(
        order_id=["ORD-1", "ORD-2"],
        order_date=["2025-01-05", "2025-02-10"],
        warehouse=["Pune", "Pune"],
        category=["Electronics", "Electronics"],
        sku=["EL-1", "EL-1"],
        stock_on_hand=[5, 100],  # restocked since the older, low-stock row
        reorder_point=[10, 10],
    )
    alerts = pd.read_csv(run_analysis(frame) / "inventory_reorder_alerts.csv")
    assert alerts.empty


def test_warns_when_unit_cost_exceeds_unit_price(run_analysis, capsys):
    run_analysis(make_rows(unit_cost=[30.0, 25.0]))
    assert "unit cost greater than unit price" in capsys.readouterr().out


# --- Input validation ---------------------------------------------------------


def test_rejects_missing_required_column(run_analysis):
    with pytest.raises(ValueError, match="Missing required columns"):
        run_analysis(make_rows().drop(columns=["sku"]))


def test_rejects_unparseable_date(run_analysis):
    with pytest.raises(ValueError, match="order_date"):
        run_analysis(make_rows(order_date=["2025-01-05", "not a date"]))


def test_rejects_non_numeric_price(run_analysis):
    with pytest.raises(ValueError, match="missing or invalid"):
        run_analysis(make_rows(unit_price=[20.0, "abc"]))


def test_rejects_negative_quantity(run_analysis):
    with pytest.raises(ValueError, match="must not be negative"):
        run_analysis(make_rows(quantity=[10, -1]))


def test_rejects_duplicate_order_ids(run_analysis):
    with pytest.raises(ValueError, match="duplicate"):
        run_analysis(make_rows(order_id=["ORD-1", "ORD-1"]))


def test_rejects_blank_sku(run_analysis):
    with pytest.raises(ValueError, match="sku"):
        run_analysis(make_rows(sku=["EL-1", None]))
