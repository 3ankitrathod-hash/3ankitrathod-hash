# Data Dictionary — Synthetic Supply Chain Orders

All rows are synthetic and created for practice. The data is not sourced from a real employer or customer.

| Column | Type | Meaning |
|---|---|---|
| order_id | Text | Unique demonstration order identifier |
| order_date | Date | Order date in ISO YYYY-MM-DD format |
| region | Category | Demonstration sales region |
| warehouse | Category | Demonstration warehouse location |
| category | Category | Product category |
| sku | Text | Stock keeping unit identifier |
| quantity | Integer | Number of units in the order |
| unit_price | Decimal | Selling price per unit, in arbitrary demo currency units |
| unit_cost | Decimal | Estimated cost per unit, in the same demo currency units |
| lead_time_days | Integer | Demonstration replenishment lead time |
| stock_on_hand | Integer | Snapshot inventory quantity |
| reorder_point | Integer | Threshold used to flag possible replenishment |

## Interpretation cautions

- Currency is intentionally unspecified; do not label these values as INR or USD.
- `stock_on_hand` and `reorder_point` are illustrative snapshot fields repeated on order rows. The reorder output deduplicates SKU/category/warehouse combinations, but a real system should use a separate inventory snapshot table.
- Sales and profit are simplified: discounts, taxes, returns, freight, storage, and other costs are excluded.
- This dataset is designed to demonstrate workflow and code, not to support real operational decisions.
