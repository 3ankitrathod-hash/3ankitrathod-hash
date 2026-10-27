# Space Mission Analysis

## Overview
Exploratory analysis of space mission records, covering mission outcomes, organizations, launch locations, yearly and decade trends, rocket status, and mission costs.

## Tools
Python, pandas, NumPy, Matplotlib, Seaborn.

## Files
- `SpaceProject.py` — analysis script.
- `data/space_mission_data.csv` — a small synthetic demonstration dataset. The mission names and records are illustrative, not verified historical mission data.
- `requirements.txt` — Python dependencies.
- `.github/workflows/space-mission-check.yml` — runs the script against the included demo CSV.

## Run locally
From this project folder:

```bash
python -m pip install -r requirements.txt
python SpaceProject.py
```

The script looks for `data/space_mission_data.csv` first and then `space_mission_data.csv` beside the script.

## Fixes
- Replaced machine-specific paths with portable local-path checks and a clear error message.
- Safely removes an optional exported index column.
- Checks required columns before running analysis.
- Cleans currency symbols and commas before converting prices to numeric values.
- Adds explicit plot colors for compatibility with current Seaborn versions.
- Missing mission dates remain missing; success-rate calculations avoid treating missing statuses as confirmed failures.

## Validation status and limitations
The repository's CSV is synthetic demonstration data and must not be presented as real space-industry findings. GitHub Actions runs the script after installing dependencies; check the Space Mission Demo Check workflow for the latest result. Interpret the output as a code demonstration only; mission-cost fields, mission status and locations are fictional in the demo file.
