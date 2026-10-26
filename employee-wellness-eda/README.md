# Employee Wellness Analysis — EDA

## Overview
Exploratory data analysis of a workplace mental-health survey dataset. The notebook focuses on data quality, consistent categories, employee age groups, and relationships between reported treatment and workplace factors.

## Tools
- Python
- pandas and NumPy
- Matplotlib and Seaborn
- Jupyter Notebook

## Analysis covered
- Inspecting dataset shape, columns, and missing values
- Cleaning implausible age values and inconsistent gender labels
- Correcting employee-size categories affected by spreadsheet date conversion
- Handling missing responses and removing free-text comments from the analysis frame
- Visualizing age and gender distributions
- Exploring treatment-seeking alongside family history, work interference, company size, and employer benefits
- Summarizing the countries represented in the survey

## Important interpretation note
This is exploratory analysis of self-reported survey responses. Associations in the data do not establish that one factor causes another, and results should not be used to diagnose individuals or make employment decisions.

## Data and reproducibility
The source notebook expects a local file named `employee_wellness_dataset.csv`. The dataset is not included in this folder. Add it locally from its permitted source before running the notebook; do not commit private or identifiable employee records.

## Project status
Documentation published; notebook and data are not yet included in this GitHub project folder.
