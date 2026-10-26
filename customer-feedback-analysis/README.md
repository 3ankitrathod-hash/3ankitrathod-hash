# Customer Feedback Analysis & Automated Apology Emails

## Overview
A Python notebook that cleans review text, flags low-rated reviews with an explainable rule, counts common complaint keywords, and drafts customer-support apology emails.

## Tools
Python, pandas, NumPy, regular expressions, Counter, Jupyter Notebook; OpenAI API is optional.

## Run locally
1. Install dependencies from `requirements.txt`.
2. Place the permitted source CSV at `data/Womens Clothing E-Commerce Reviews.csv`.
3. Run `customer_feedback_analysis.ipynb` from top to bottom.
4. Set `OPENAI_API_KEY` as an environment variable only if you want to attempt real API calls.

## Fixes and safeguards
- The notebook no longer stops with an error when fewer than three critical reviews exist; it selects up to three.
- API errors fall back to a clearly labelled mock email.
- Never hard-code or commit API keys.
- Review text is sent to the external API only when the API is enabled. Do not send confidential or identifiable customer data unless you are authorized to do so.
- The 1–2 star threshold and keyword counting are simple rules, not a trained sentiment model.

## Validation status
- Python cells pass syntax parsing.
- The notebook completed a runtime test with a temporary synthetic review dataset.
- The original review CSV was not available for this repair pass, so final counts and business findings need verification against the permitted source data.
