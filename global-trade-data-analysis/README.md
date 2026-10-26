# Global Trade Data Analysis — Excel

## Overview
Excel data-cleaning and summary analysis of 500 trade-order rows, using order dates, countries, products, categories, sales, shipping costs, profit, and region codes.

## Final workbook
The repaired workbook is prepared locally as `Global_Trade_Data_Analysis_Final.xlsx`. It contains Raw_Data, Clean_Data, Summary_Tables, and Read_Me sheets.

## Fixes and checks
- Standardized common country abbreviations such as USA, UK, and UAE.
- Converted order dates and formatted them as month-year.
- Applied currency formatting to unit price, total sales, shipping cost, and profit.
- Highlighted negative profits.
- Replaced customer names with pseudonymous labels in the portfolio workbook.
- Added KPI formulas and SUMIFS/AVERAGEIFS summaries by Region_Code and Category.
- Checked 500 unique order IDs and verified that Total_Sales matches Quantity × Unit_Price within a small rounding tolerance.

## Validation status
The workbook was recalculated in LibreOffice and checked for formula errors. The source dataset has no negative-profit rows, so the conditional formatting is present but does not highlight any current records.
