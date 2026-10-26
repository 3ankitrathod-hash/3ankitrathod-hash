# Healthcare Analytics Database — SQL Practice

## Overview

SQL practice using a relational healthcare schema and reporting questions about patients, doctors, appointments, bills, and departments.

## Files

- healthcare_schema.sql — safe schema-only version; no database-drop command and no sample personal records.
- healthcare_queries.sql — MySQL 8 queries for patient filtering, doctor experience, patient counts, paid bills, department revenue, and a vw_doctor_revenue view.

## Run locally

1. Open a disposable MySQL 8 practice environment.
2. Run healthcare_schema.sql to create the practice database and tables.
3. Add fictional test rows that satisfy the table constraints.
4. Run healthcare_queries.sql and inspect each result set.
5. Capture results and note the database version after successful execution.

The schema is intentionally empty, so queries will return no business records until test data is inserted.

## Safety

The original coursework file included a destructive database-drop statement and records containing name/contact/address-like fields. That raw file has not been uploaded. The published schema-only version does not include those sample records and does not drop a database. Never upload real patient records or personally identifiable health information.

## Validation status

The schema and query structure have been reviewed, but a live MySQL 8 execution has not been completed here. Do not describe the queries as runtime-validated until you run them and check the results.
