# Olympic Athlete Analysis

## Overview
This project uses Exploratory Data Analysis (EDA) to study Olympic athlete-event records from 1896 to 2016. The analysis explores participation over time, athlete demographics, sports, countries/NOCs, and medal outcomes.

## Objectives
- Understand the dataset structure and the fact that each row represents an athlete-event record.
- Check data quality, duplicates, and missing values.
- Clean the data using documented rules.
- Explore trends with Python and visualizations.
- Summarize findings and limitations clearly.

## Tools
- Python
- pandas and NumPy
- Matplotlib and Seaborn
- Jupyter Notebook

## Data preparation
The project notebook reports 271,116 original records. After removing 1,385 exact duplicate rows, the cleaned dataset contains 269,731 records and 17 columns. Missing medal values are treated as **No Medal**; missing Age, Height, and Weight values are imputed using group medians with an overall-median fallback. Potential outliers are investigated rather than automatically deleted.

## Key findings
- The dataset covers Olympic Games from 1896 through 2016.
- Female participation rises substantially over the historical period.
- Athletics, Gymnastics, and Swimming are among the most represented sports.
- Summer Olympic records substantially outnumber Winter Olympic records.
- Most athlete-event records do not include a medal.
- The analysis explores how participation and athlete measurements vary by sport and time.

These findings describe records in this dataset; they should not be interpreted as counts of unique athletes unless the analysis explicitly deduplicates by athlete ID.

## Project status
This README documents the project. The notebook and any required dataset still need to be uploaded to this GitHub project location before the project can be reproduced from GitHub.

## How to run
1. Install Python and Jupyter Notebook.
2. Install the required libraries:
   `pip install pandas numpy matplotlib seaborn jupyter`
3. Place the dataset file in the project folder.
4. Open the notebook and update the dataset path to match the local file location.
5. Run the notebook cells from top to bottom.

## Limitations
- The dataset ends in 2016.
- Athlete-event records are not the same as unique-athlete counts.
- Median imputation can reduce natural variation.
- The project is exploratory; associations in charts do not establish causation.

## Author
Ankit Rathod
