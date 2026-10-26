# Space Mission Analysis

## Overview
Exploratory analysis of space mission records, covering mission outcomes, organizations, launch locations, yearly and decade trends, rocket status, and mission costs.

## Tools
Python, pandas, NumPy, Matplotlib, Seaborn.

## Files
- `SpaceProject.py` — repaired analysis script.
- `requirements.txt` — Python dependencies.

## Run locally
1. Install dependencies from `requirements.txt`.
2. Place `space_mission_data.csv` in the `data/` folder or beside the script.
3. Run `python SpaceProject.py`.

## Fixes
- Replaced the machine-specific Windows path with a portable local-path check and a clear error message.
- Safely removes an optional exported index column.
- Checks required columns before running analysis.
- Cleans currency symbols and commas before converting prices to numeric values.
- Adds explicit plot colors for compatibility with current Seaborn versions.
- Missing mission dates remain missing; success rate calculations avoid treating missing statuses as confirmed failures.

## Validation status
The script compiled and completed a runtime test using a temporary synthetic dataset. The original space-mission CSV was not available for this repair pass, so the original-data findings and price distribution have not been revalidated.
