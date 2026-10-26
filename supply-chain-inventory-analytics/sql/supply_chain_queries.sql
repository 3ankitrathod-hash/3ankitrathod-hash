-- Supply Chain & Inventory Analytics (MySQL 8+)
-- Create a table and import data/supply_chain_orders.csv before running.
-- Data is synthetic demonstration data; do not interpret as real business results.

-- 1. Overall sales, estimated cost, profit, and margin
SELECT
    COUNT(DISTINCT order_id) AS order_count,
    SUM(quantity) AS total_units,
    ROUND(SUM(quantity * unit_price), 2) AS total_sales,
    ROUND(SUM(quantity * unit_cost), 2) AS estimated_cost,
    ROUND(SUM(quantity * (unit_price - unit_cost)), 2) AS gross_profit,
    ROUND(
        100 * SUM(quantity * (unit_price - unit_cost))
        / NULLIF(SUM(quantity * unit_price), 0), 2
    ) AS gross_margin_pct
FROM supply_chain_orders;

-- 2. Category performance
SELECT
    category,
    SUM(quantity * unit_price) AS sales,
    SUM(quantity * (unit_price - unit_cost)) AS gross_profit,
    ROUND(
        100 * SUM(quantity * (unit_price - unit_cost))
        / NULLIF(SUM(quantity * unit_price), 0), 2
    ) AS gross_margin_pct
FROM supply_chain_orders
GROUP BY category
ORDER BY sales DESC;

-- 3. Monthly sales and profit trend
SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS sales_month,
    COUNT(DISTINCT order_id) AS order_count,
    SUM(quantity * unit_price) AS sales,
    SUM(quantity * (unit_price - unit_cost)) AS gross_profit
FROM supply_chain_orders
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY sales_month;

-- 4. Region performance
SELECT
    region,
    SUM(quantity * unit_price) AS sales,
    SUM(quantity * (unit_price - unit_cost)) AS gross_profit,
    COUNT(DISTINCT order_id) AS order_count
FROM supply_chain_orders
GROUP BY region
ORDER BY sales DESC;

-- 5. Warehouse performance
SELECT
    warehouse,
    SUM(quantity * unit_price) AS sales,
    AVG(lead_time_days) AS avg_lead_time_days,
    COUNT(DISTINCT order_id) AS order_count
FROM supply_chain_orders
GROUP BY warehouse
ORDER BY sales DESC;

-- 6. Inventory reorder candidates (snapshot fields in the synthetic dataset)
SELECT DISTINCT
    sku, category, warehouse, stock_on_hand, reorder_point, lead_time_days
FROM supply_chain_orders
WHERE stock_on_hand <= reorder_point
ORDER BY warehouse, category, sku;

-- 7. Products with the largest estimated profit contribution
SELECT
    sku,
    category,
    SUM(quantity * (unit_price - unit_cost)) AS gross_profit
FROM supply_chain_orders
GROUP BY sku, category
ORDER BY gross_profit DESC
LIMIT 10;
