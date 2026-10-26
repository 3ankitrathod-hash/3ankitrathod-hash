# Employee Wellness Analysis — EDA

## Overview
A Jupyter notebook for aggregate exploratory analysis of a workplace wellness survey. The repaired notebook restores the broken Python cell formatting, uses robust local dataset-path checks, improves age and category cleaning, and avoids treating missing answers as a definite “No.”

## Tools
Python, pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook.

## Run locally
1. Install Python 3.10+.
2. Install the dependencies from `requirements.txt`.
3. Obtain the source CSV only from a source whose terms permit your use.
4. Place `employee_wellness_dataset.csv` in `data/` or beside the notebook.
5. Run `Employee_Wellness_EDA.ipynb` from top to bottom.

## Privacy and interpretation
The source survey includes sensitive workplace mental-health responses. Do not publish identifiable records or free-text comments. Use only aggregate analysis; do not diagnose, rank, or make employment decisions about individuals. Associations are not proof of causation.

## Validation status
- All repaired Python cells pass syntax parsing.
- The notebook completed a runtime test using a temporary synthetic dataset.
- The original survey CSV was not available for this repair pass, so real-data percentages and narrative claims still need rechecking against the permitted dataset.
