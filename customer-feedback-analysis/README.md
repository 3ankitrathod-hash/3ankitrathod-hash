# Customer Feedback Analysis & Automated Apology Emails

## Overview
A Python notebook that cleans customer review text, identifies low-rated reviews with a transparent rule, counts common complaint keywords, and drafts short customer-support apology emails.

## Tools
- Python
- pandas and NumPy
- Regular expressions and Counter
- OpenAI API (optional)
- Jupyter Notebook

## Workflow
1. Load the review rating and review-text columns.
2. Remove records without a usable rating or review.
3. Normalize review text for keyword analysis.
4. Flag reviews rated 1 or 2 stars as critical.
5. Count complaint-related words after basic stopword filtering.
6. Select up to three detailed critical reviews for example responses.
7. Generate draft apology emails using the API when configured, or a clearly labelled mock template when it is not.

## Safety and limitations
- The 1–2 star threshold is a simple rule, not a machine-learning classifier.
- Keyword counts depend on the small, editable stopword list and may miss context, sarcasm, or language variation.
- Generated emails should be reviewed by a person before sending.
- Never commit API keys or private customer data. The notebook reads `OPENAI_API_KEY` from an environment variable.

## Data and reproducibility
The notebook expects the public review CSV at `data/Womens Clothing E-Commerce Reviews.csv`. The data file is not included here; obtain it from a source whose terms permit your use.

## Project status
Documentation published; notebook and dataset are not yet included in this GitHub project folder.
