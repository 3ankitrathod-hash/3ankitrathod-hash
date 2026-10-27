# Power BI Dashboard Build Guide

## Files
- `Supply_Chain_Dashboard_Measures.dax` — measures to create after importing the source CSV.
- Source data: `../data/supply_chain_orders.csv`
- Reorder candidates: `../outputs/inventory_reorder_alerts.csv`

## 1. Import the data
1. Open Power BI Desktop.
2. Select **Get data → Text/CSV** and load `data/supply_chain_orders.csv`.
3. Name the table `supply_chain_orders`.
4. Set `order_date` to Date; set quantity, price, cost, lead time, stock, and reorder point to numeric types.
5. Load `outputs/inventory_reorder_alerts.csv` as a separate table named `inventory_reorder_alerts`.

## 2. Add measures
Open **Modeling → New measure** and add the measures from `Supply_Chain_Dashboard_Measures.dax` one by one. The DAX file is a reference text file; it is not a Power BI project file and does not create a PBIX automatically.

## 3. Recommended one-page layout
- Top row: Total Sales, Estimated Gross Profit, Estimated Gross Margin %, Unique Orders, Units Sold.
- Middle left: line chart with month on the X-axis and Total Sales / Estimated Gross Profit as values.
- Middle right: bar chart of Total Sales by category.
- Bottom left: bar chart of Estimated Gross Profit by region.
- Bottom right: table from `inventory_reorder_alerts` with SKU, category, warehouse, stock_on_hand, reorder_point, and lead_time_days.
- Slicers: order_date, region, category, warehouse.

## 4. Validate before publishing
- Compare KPI cards with `outputs/kpi_summary.csv`.
- Compare monthly totals with `outputs/monthly_sales.csv`.
- Compare category totals with `outputs/category_summary.csv`.
- Use the separate reorder-alert CSV for inventory candidates; stock fields are repeated on order rows and should not be summed as if each row were a new inventory snapshot.
- Keep currency labels as unspecified demo currency units unless the dataset owner confirms a currency.
- Save the finished file as `Supply_Chain_Inventory_Dashboard.pbix` and add genuine screenshots only after checking the report.

## Current status
This guide and DAX measures are committed, but the actual PBIX still must be created in Power BI Desktop. Do not describe the dashboard as finished until the PBIX exists and has been checked.
