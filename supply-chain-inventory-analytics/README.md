# Supply Chain & Inventory Analytics

An end-to-end beginner portfolio project showing how an analyst can turn order-level data into sales, estimated margin, monthly trend, category performance, and inventory-reorder reporting.

> **Data note:** The CSV contains synthetic demonstration data. It does not represent a real company, supplier, customer, or shipment.

## Business questions

1. What are total sales, estimated cost, gross profit, and gross margin?
2. Which product categories contribute the most sales and estimated profit?
3. How do sales change month to month?
4. Which SKU/warehouse combinations are at or below the reorder point?
5. How do regions and warehouses compare?

## Tools and files

- data/supply_chain_orders.csv — synthetic order/inventory dataset
- analyze_supply_chain.py — data checks, calculations, summaries, and charts
- sql/supply_chain_queries.sql — MySQL 8 query examples
- DATA_DICTIONARY.md — field definitions and limitations
- requirements.txt — Python dependencies
- .github/workflows/supply-chain-check.yml — automated analysis check

## Run locally

From this directory, create and activate a virtual environment, then run:

    python -m pip install -r requirements.txt
    python analyze_supply_chain.py

The script creates an outputs folder containing KPI, category, monthly, regional, warehouse, and reorder CSV summaries plus PNG charts. Outputs are generated locally and are not automatically committed.

## Power BI dashboard specification

Import data/supply_chain_orders.csv into Power BI Desktop. Create these visuals:

- KPI cards: Total Sales, Estimated Gross Profit, Estimated Gross Margin %, Unique Orders, Units Sold.
- Line chart: Monthly Sales and Estimated Gross Profit.
- Bar chart: Sales by Category.
- Bar chart: Estimated Gross Profit by Region.
- Table: SKU, Category, Warehouse, Stock On Hand, Reorder Point, Lead Time Days, Reorder Flag.
- Slicers: Order Date, Region, Category, Warehouse.

Suggested DAX measures after importing the CSV as supply_chain_orders:

    Total Sales = SUMX(supply_chain_orders, supply_chain_orders[quantity] * supply_chain_orders[unit_price])
    Estimated Cost = SUMX(supply_chain_orders, supply_chain_orders[quantity] * supply_chain_orders[unit_cost])
    Estimated Gross Profit = [Total Sales] - [Estimated Cost]
    Estimated Gross Margin % = DIVIDE([Estimated Gross Profit], [Total Sales], 0)
    Unique Orders = DISTINCTCOUNT(supply_chain_orders[order_id])
    Units Sold = SUM(supply_chain_orders[quantity])

Save the dashboard as Supply_Chain_Inventory_Dashboard.pbix. Add the PBIX and screenshots only after actually building and checking them; no Power BI file is currently included.

## Metric definitions and limitations

- Sales = quantity × unit price
- Estimated cost = quantity × unit cost
- Estimated gross profit = sales − estimated cost
- Estimated gross margin % = estimated gross profit ÷ sales × 100
- Reorder flag = stock on hand less than or equal to reorder point

Currency is intentionally unspecified. The data excludes discounts, taxes, returns, freight, storage, supplier constraints, demand variability, and service-level targets. Inventory values are illustrative snapshots repeated on order rows; real replenishment decisions should use a separate inventory snapshot and consider lead times and demand.

## Validation status

The Python script checks required columns, dates, numeric values, duplicate order IDs, and output generation. Review GitHub Actions status and inspect generated summaries before reporting exact numeric findings. SQL examples are MySQL 8 style and still need to be run against an imported table in MySQL 8.

## Next improvements

1. Run and compare Python and SQL totals.
2. Build and verify the Power BI dashboard.
3. Add genuine Power BI screenshots and a data-backed findings section.
4. Try a licensed public supply-chain dataset for a separate real-world analysis.
