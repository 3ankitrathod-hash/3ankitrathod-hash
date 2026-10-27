# Employee Wellness Analysis — EDA

## Overview
A Jupyter notebook for aggregate exploratory analysis of workplace wellness survey responses. It cleans age and categories, preserves uncertainty in missing answers, and creates aggregate summaries and charts.

## Project files
- `Employee_Wellness_EDA.ipynb` — analysis notebook.
- `data/employee_wellness_dataset.csv` — a small survey extract in the repository. Its provenance and completeness have not been independently verified; it should not be described as the full original survey without checking the source.
- `data/employee_wellness_dataset_demo.csv` — clearly synthetic rows used for automated notebook execution.
- `requirements.txt` — Python dependencies.
- `.github/workflows/notebook-demo-check.yml` — executes the notebook in synthetic demo mode.

## Run locally
1. Install dependencies: `pip install -r requirements.txt`.
2. From this project folder, run the notebook normally to use the included survey extract.
3. To force the synthetic demo mode in a terminal, set `PORTFOLIO_DEMO_MODE=1` before launching Jupyter. On Windows PowerShell: `$env:PORTFOLIO_DEMO_MODE="1"; jupyter notebook`. On macOS/Linux: `PORTFOLIO_DEMO_MODE=1 jupyter notebook`.
4. Verify the survey source, license, and whether the extract is appropriate before reporting results.

## Privacy and interpretation
The survey topic includes sensitive workplace mental-health responses. Do not publish identifiable records or free-text comments. Use aggregate analysis only; do not diagnose, rank, or make employment decisions about individuals. Associations are not proof of causation.

## Validation status
GitHub Actions executes the notebook with synthetic demo rows to detect code and dependency errors. Demo outputs are not real employee findings. Any analysis of the included survey extract must be reviewed separately, and all counts and narrative claims must be rechecked against a permitted, documented source.
