# Olympic Athlete Analysis — Exploratory Data Analysis (EDA)

## Overview
Exploratory analysis of Olympic athlete-event records from 1896 to 2016, including data quality checks, cleaning, descriptive statistics, and visual storytelling.

## Project files
- `Olympic_Athlete_Analysis_Final.ipynb` — cleaned Jupyter notebook with code and explanations; saved outputs cleared for reproducibility.
- `requirements.txt` — Python dependencies.
- `.gitignore` — excludes local environments, checkpoints, and generated cleaned CSV files.

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
3. Install dependencies with `pip install -r requirements.txt`.
4. Obtain the CSV from a source whose terms permit your use. The dataset is not included in this repository.
5. Place the CSV at `data/athlete_data.csv` or beside the notebook.
6. Open Jupyter Notebook and run cells from top to bottom.

Expected columns include `ID`, `Sex`, `Age`, `Height`, `Weight`, `NOC`, `Year`, `Season`, `Sport`, `Event`, and `Medal`.

## Dataset checks and findings
The supplied dataset version used during testing contained 271,116 rows and 15 columns. Removing 1,385 exact duplicate rows left 269,731 records. The dataset covers Olympic records through Rio 2016. These figures should be rechecked if a different CSV version is used.

The notebook completed a full run against the dataset available in the working files. The repository copy has saved cell outputs cleared, so readers can reproduce the analysis with their own permitted copy of the dataset.

## Limitations
- The dataset ends in 2016.
- Each row is an athlete-event record, not necessarily a unique athlete.
- NOC codes are shown as provided.
- Median imputation can reduce natural variation.
- This is descriptive analysis; associations do not establish causation.
