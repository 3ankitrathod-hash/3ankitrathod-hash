# Employee Wellness Analysis — EDA

## Overview
A Jupyter notebook for aggregate exploratory analysis of a workplace wellness survey. It cleans age and categories, preserves uncertainty in missing answers, and creates aggregate summaries and charts.

## Project files
- `Employee_Wellness_EDA.ipynb` — analysis notebook.
- `data/employee_wellness_dataset_demo.csv` — fictional demonstration rows for reproducible code testing.
- `requirements.txt` — Python dependencies.
- `.github/workflows/notebook-demo-check.yml` — executes this notebook using the synthetic demo.

## Run locally
1. Install Python 3.10+ and dependencies with `pip install -r requirements.txt`.
2. Run the notebook from this project folder. If the original `employee_wellness_dataset.csv` is absent, it uses the demo CSV and prints a warning.
3. For real-data analysis, obtain the permitted source and place it at `data/employee_wellness_dataset.csv`; it takes precedence over the demo.

## Privacy and interpretation
The original survey topic includes sensitive workplace mental-health responses. Do not publish identifiable records or free-text comments. Use aggregate analysis only; do not diagnose, rank, or make employment decisions about individuals. Associations are not proof of causation.

## Validation status
GitHub Actions executes the notebook with synthetic demo rows to detect code and dependency errors. These outputs are not real employee findings. Recheck percentages and narrative claims against the permitted original dataset before reporting results.
