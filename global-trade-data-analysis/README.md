# Global Trade Data Analysis — Excel

## Overview
Excel data-cleaning and summary analysis coursework using trade-order fields such as order dates, countries, products, categories, sales, shipping costs, profit, and region codes. This is an educational sample, not real commercial performance.

## Files
- `Global_Trade_Data_Analysis_Final.xlsx` — committed workbook; inspect the workbook's sheets before interpreting results.
- `workbook_kpis.csv` — compact KPI summary currently copied from the workbook.
- `summary-preview.svg` — recreated visual preview from summary values, not an Excel screenshot.
- `.github/workflows/global-trade-validation.yml` — automated workbook integrity and KPI-summary checks.

## KPI preview

![Global Trade KPI summary preview](./summary-preview.svg)

| KPI | Current documented value |
|---|---:|
| Total orders | 500 |
| Total sales (USD) | $474,704.62 |
| Total profit (USD) | $133,570.40 |
| Average order value (USD) | $949.41 |
| Orders with negative profit | 0 |

These are the values currently stored in `workbook_kpis.csv`; they are not certified until the workflow confirms the workbook structure and arithmetic. Do not quote these as independently verified findings until the validation run passes.

## Analysis workflow
- Standardize country names and trim extra spaces.
- Convert order dates and format them as month-year.
- Apply currency formatting to unit price, total sales, shipping cost, and profit.
- Highlight negative profits using conditional formatting.
- Use pseudonymous labels if customer fields are included in a public portfolio copy.
- Add KPI formulas and SUMIFS/AVERAGEIFS summaries by Region_Code and Category.
- Validate order IDs and check whether Total_Sales agrees with Quantity × Unit_Price within a rounding tolerance.

## Validation and limitations
The workflow checks that the workbook opens, that expected worksheets exist, and that the KPI CSV is parseable. It does not replace a manual review of formulas, pivot tables, conditional formatting, or the underlying cleaning steps. Review the workflow run and workbook sheets before presenting the project.

Do not publish customer names or private data. Only share the workbook if its source data is permitted for public distribution.
