# Supply Chain & Inventory Analytics

An end-to-end beginner portfolio project showing how an analyst can turn order-level data into sales, margin, monthly trend, category performance, and inventory-reorder reporting.

> **Data note:** The included CSV is synthetic demonstration data generated for this portfolio. It does not represent a real company, supplier, customer, or shipment.

## Business questions

1. What are total sales, estimated cost, gross profit, and gross margin?
2. Which product categories contribute the most sales and profit?
3. How do sales change month to month?
4. Which SKUs are at or below their reorder point?
5. Which regions and warehouses contribute to sales?

## Tools

- Python 3.10+
- pandas and Matplotlib
- SQL (MySQL 8-compatible query examples)
- CSV as the portable source format

## Repository contents

- `data/supply_chain_orders.csv` — synthetic order/inventory dataset
- `analyze_supply_chain.py` — analysis script and chart generation
- `sql/supply_chain_queries.sql` — SQL business questions
- `requirements.txt` — Python dependencies
- `outputs/` — generated reports and charts after running the script

## Run it locally

From this project directory:

```bash
python -m venv .venv
```

Windows:
```bash
.venv\\Scripts\\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install dependencies and run:

```bash
pip install -r requirements.txt
python analyze_supply_chain.py
```

The script creates an `outputs` folder with:
- `kpi_summary.csv`
- `category_summary.csv`
- `monthly_sales.csv`
- `inventory_reorder_alerts.csv`
- `sales_by_category.png`
- `monthly_sales_trend.png`

## Metric definitions

- **Sales** = quantity × unit price
- **Estimated cost** = quantity × unit cost
- **Gross profit** = sales − estimated cost
- **Gross margin %** = gross profit ÷ sales × 100
- **Reorder flag** = stock on hand less than or equal to reorder point

These are simplified portfolio metrics. The dataset does not model returns, discounts, tax, stock movements, supplier constraints, or service-level targets.

## Data checks in the script

- Parses order dates and numeric columns
- Checks for missing values and duplicate order IDs
- Calculates derived sales, cost, and profit columns
- Sorts monthly reporting periods chronologically
- Exports reorder candidates separately

## SQL practice

The SQL file contains queries for sales/profit KPIs, category and region performance, monthly trends, warehouse performance, and reorder candidates. The CSV is the source of truth for the Python version. To execute SQL, create a table with matching columns and load the CSV into a local MySQL database.

## Results and interpretation

Run the script first, then review the generated CSVs and charts before writing numeric findings. This README intentionally does not claim business results before execution. In an interview, explain the metric definitions, data limitations, and how you would validate stock levels against a real inventory system.

## Next improvements

- Load the data into MySQL and compare SQL outputs with Python totals
- Build a Power BI dashboard with KPI cards, monthly sales, category margin, and reorder alerts
- Add screenshots after validating the output
- Test with a larger real public dataset where licensing permits
