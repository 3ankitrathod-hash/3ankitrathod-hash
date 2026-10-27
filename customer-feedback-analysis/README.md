# Customer Feedback Analysis & Automated Apology Emails

## Overview
A Python notebook that cleans review text, flags low-rated reviews using an explainable rule, counts common complaint keywords, and drafts customer-support apology emails. The OpenAI API is optional.

## Project files
- `customer_feedback_analysis.ipynb` — analysis and draft-email workflow.
- `data/Womens Clothing E-Commerce Reviews_demo.csv` — clearly labeled synthetic review examples for reproducible testing.
- `requirements.txt` — notebook dependencies.
- `.github/workflows/notebook-demo-check.yml` — executes this notebook using the synthetic demo.

## Run locally
1. Install dependencies with `pip install -r requirements.txt`.
2. Run the notebook from this project folder. If the original `data/Womens Clothing E-Commerce Reviews.csv` is absent, the notebook uses the synthetic demo CSV and prints a warning.
3. For analysis of real reviews, obtain the permitted original dataset and save it as `data/Womens Clothing E-Commerce Reviews.csv`; it takes precedence over the demo.
4. Set `OPENAI_API_KEY` as an environment variable only if you intentionally want to enable the external API. Without a key, the notebook uses a labeled mock fallback.

## Fixes and safeguards
- Handles fewer than three critical reviews without stopping.
- API errors fall back to a clearly labeled mock email.
- Never hard-code or commit API keys.
- Do not send confidential or identifiable customer data to an external API unless authorized.
- The 1–2 star threshold and keyword counting are simple rules, not a trained sentiment model.

## Validation status
GitHub Actions executes the notebook against the synthetic demo data. Those results are for software testing only, not real customer findings. Re-run with the permitted original dataset and verify all counts before reporting business conclusions.
