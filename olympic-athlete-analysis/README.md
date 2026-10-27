# Olympic Athlete Analysis — Exploratory Data Analysis (EDA)

## Overview
Exploratory analysis of athlete-event records covering participation, athlete characteristics, sports, NOCs, medal outcomes, and trends. The original Olympic dataset is not committed here.

## Project files
- `Olympic_Athlete_Analysis_Final.ipynb` — reproducible Jupyter notebook with code and explanations.
- `data/athlete_data_demo.csv` — small, fictional demonstration dataset included to test the notebook workflow.
- `requirements.txt` — Python dependencies.
- `.github/workflows/notebook-demo-check.yml` — runs the notebook using the synthetic demonstration data.

## Run
1. Install Python 3.10+ and dependencies: `pip install -r requirements.txt`.
2. For the demo, run the notebook from this project folder; it automatically uses `data/athlete_data_demo.csv` if the original file is absent.
3. For real analysis, obtain a permitted Olympic athlete-event dataset and place it at `data/athlete_data.csv`. The original dataset takes precedence over the demo file.
4. Run the notebook from top to bottom.

## Analysis included
- Dataset shape, data types, missing values, and exact duplicate assessment
- Cleaning missing medal labels and imputing age, height, and weight
- Participation trends by year and season
- Sex distribution, top sports and NOCs
- Medal records by NOC and sport
- Age, height, and weight distributions
- Medal outcomes by sex and Summer/Winter participation
- Female participation over time and age-versus-weight relationship

## Validation status
GitHub Actions executes the notebook with the synthetic demonstration CSV to catch code and workflow errors. **Demo output is not evidence about actual Olympic history.** The original full dataset was not available during this pass, so its previously documented row counts and real-data findings must be rechecked against the exact source file before quoting them.

## Limitations
- Results depend on the dataset version and data-cleaning choices.
- Each row represents an athlete-event record, not necessarily a unique athlete.
- Median imputation can reduce natural variation.
- This is descriptive analysis; associations do not establish causation.
