# Olympic Athlete Analysis — Exploratory Data Analysis (EDA)

## Overview
An exploratory analysis of Olympic athlete-event records from 1896 to 2016. The notebook demonstrates data inspection, quality checks, cleaning, feature engineering, descriptive statistics, and visual storytelling.

## Project files
- `Olympic_Athlete_Analysis_Final.ipynb` — cleaned Jupyter notebook with code and markdown explanations. Saved outputs have been cleared so results can be reproduced locally.
- `requirements.txt` — Python dependencies.
- `.gitignore` — excludes local environments, checkpoints, and the generated cleaned CSV.

## Tools
Python, pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook.

## Analysis included
- Dataset structure, data types, and missing values
- Exact duplicate-row assessment and removal
- Missing medal values represented as `No Medal`
- Median imputation for age, height, and weight using sport-and-sex groups, then overall medians as a fallback
- Participation trends, sex distribution, top sports and NOCs
- Medal records by NOC and sport
- Age, height, and weight distributions
- Medal outcomes by sex and Summer/Winter participation
- Female participation over time
- Age-versus-weight relationship and medal distribution

## How to run
1. Install Python 3.10+.
2. Clone or download this repository.
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Obtain the dataset from a source whose terms permit your use. The dataset is not included in this repository.
5. Place the CSV at `data/athlete_data.csv` relative to the notebook, or place `athlete_data.csv` beside the notebook.
6. Start Jupyter Notebook and run the cells from top to bottom.

The notebook expects columns including `ID`, `Sex`, `Age`, `Height`, `Weight`, `NOC`, `Year`, `Season`, `Sport`, `Event`, and `Medal`.

## Key findings reported in the analysis
- The supplied dataset contains 271,116 rows and 15 columns before cleaning.
- 1,385 exact duplicate rows are removed, leaving 269,731 records.
- The dataset covers Olympic records through Rio 2016.
- Female participation increases over the period represented in the data.
- Athlete-event counts are not the same as unique-athlete counts because one athlete may participate in multiple events.

These figures describe the dataset version used in the notebook. They should be rechecked if a different CSV version is used.

## Limitations
- The dataset ends in 2016 and does not cover later Olympic Games.
- Each row is an athlete-event record, not necessarily a unique athlete.
- NOC codes are shown as provided; country names are not inferred.
- Median imputation can reduce natural variation, so imputed measurements should be interpreted carefully.
- Outliers are retained when they may represent valid observations.
- This is descriptive analysis; observed relationships do not establish causation.

## Reproducibility status
The notebook was run successfully against the project CSV available in the working files. The dataset is intentionally not committed here; users must supply an appropriately licensed copy before running the notebook.
