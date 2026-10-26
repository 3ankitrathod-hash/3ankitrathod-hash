# Healthcare Analytics Database — SQL Practice

## Overview

SQL practice using a relational healthcare schema and reporting questions about patients, doctors, appointments, bills, and departments.

## Files

- healthcare_schema.sql — safe schema-only version; no database-drop command and no sample personal records.
- healthcare_sample_data.sql — fictional test rows for local practice and automated checks only.
- healthcare_queries.sql — MySQL 8 queries for patient filtering, doctor experience, patient counts, paid bills, department revenue, and a vw_doctor_revenue view.
- .github/workflows/healthcare-sql-check.yml — starts MySQL 8, loads the schema and fictional test rows, then executes the queries on pushes and pull requests.

## Run locally

1. Open a disposable MySQL 8 practice environment.
2. Run healthcare_schema.sql.
3. Run healthcare_sample_data.sql to load fictional test records.
4. Run healthcare_queries.sql and inspect each result set.
5. Compare your results with the successful GitHub Actions run after it finishes.

## Safety

The original coursework file included a destructive database-drop statement and records containing name/contact/address-like fields. That raw file has not been uploaded. The published schema-only version does not include those original records and does not drop a database. The added sample records are fictional. Never upload real patient records or personally identifiable health information.

## Validation status

The MySQL 8 GitHub Actions workflow has been added to execute the schema, fictional seed data, queries, and view. Check the workflow status before claiming validation has passed.
