from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "supply_chain_orders.csv"
OUTPUT_DIR = BASE_DIR / "outputs"


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    df = pd.read_csv(DATA_PATH)

    required = {
        "order_id", "order_date", "region", "warehouse", "category", "sku",
        "quantity", "unit_price", "unit_cost", "lead_time_days",
        "stock_on_hand", "reorder_point"
    }
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    numeric = [
        "quantity", "unit_price", "unit_cost", "lead_time_days",
        "stock_on_hand", "reorder_point"
    ]
    for column in numeric:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    if df["order_date"].isna().any():
        raise ValueError("Some order_date values could not be parsed.")
    if df[numeric].isna().any().any():
        raise ValueError("Numeric columns contain missing or invalid values.")
    if (df[["quantity", "unit_price", "unit_cost"]] < 0).any().any():
        raise ValueError("Quantity and price/cost values must not be negative.")
    if df["order_id"].duplicated().any():
        raise ValueError("Duplicate order_id values found; inspect source data.")

    df["sales"] = df["quantity"] * df["unit_price"]
    df["estimated_cost"] = df["quantity"] * df["unit_cost"]
    df["gross_profit"] = df["sales"] - df["estimated_cost"]
    df["gross_margin_pct"] = (
        df["gross_profit"].div(df["sales"].where(df["sales"].ne(0))).mul(100)
    )
    df["month"] = df["order_date"].dt.to_period("M").astype(str)
    df["reorder_flag"] = df["stock_on_hand"] <= df["reorder_point"]

    total_sales = df["sales"].sum()
    total_profit = df["gross_profit"].sum()
    total_cost = df["estimated_cost"].sum()
    kpis = pd.DataFrame([
        {"metric": "order_count", "value": int(df["order_id"].nunique())},
        {"metric": "total_units", "value": int(df["quantity"].sum())},
        {"metric": "total_sales", "value": round(total_sales, 2)},
        {"metric": "estimated_cost", "value": round(total_cost, 2)},
        {"metric": "gross_profit", "value": round(total_profit, 2)},
        {"metric": "gross_margin_pct", "value": round(total_profit / total_sales * 100, 2) if total_sales else 0},
        {"metric": "reorder_candidate_rows", "value": int(df["reorder_flag"].sum())},
        {"metric": "unique_skus", "value": int(df["sku"].nunique())},
    ])
    kpis.to_csv(OUTPUT_DIR / "kpi_summary.csv", index=False)

    category = df.groupby("category", as_index=False).agg(
        order_count=("order_id", "nunique"),
        units=("quantity", "sum"),
        sales=("sales", "sum"),
        estimated_cost=("estimated_cost", "sum"),
        gross_profit=("gross_profit", "sum"),
    )
    category["gross_margin_pct"] = (
        category["gross_profit"].div(category["sales"].where(category["sales"].ne(0))).mul(100)
    ).round(2)
    category = category.sort_values("sales", ascending=False)
    category.to_csv(OUTPUT_DIR / "category_summary.csv", index=False)

    monthly = df.groupby("month", as_index=False).agg(
        order_count=("order_id", "nunique"),
        units=("quantity", "sum"),
        sales=("sales", "sum"),
        gross_profit=("gross_profit", "sum"),
    ).sort_values("month")
    monthly.to_csv(OUTPUT_DIR / "monthly_sales.csv", index=False)

    alerts = df.loc[df["reorder_flag"], [
        "sku", "category", "warehouse", "stock_on_hand", "reorder_point", "lead_time_days"
    ]].drop_duplicates().sort_values(["warehouse", "category", "sku"])
    alerts.to_csv(OUTPUT_DIR / "inventory_reorder_alerts.csv", index=False)

    plt.figure(figsize=(9, 5))
    plt.bar(category["category"], category["sales"])
    plt.title("Sales by Product Category")
    plt.xlabel("Category")
    plt.ylabel("Sales")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "sales_by_category.png", dpi=160)
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.plot(monthly["month"], monthly["sales"], marker="o")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.xticks(rotation=45, ha="right")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "monthly_sales_trend.png", dpi=160)
    plt.close()

    print("Analysis completed.")
    print(kpis.to_string(index=False))
    print(f"Outputs saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
