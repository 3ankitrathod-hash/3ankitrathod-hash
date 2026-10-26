# Healthcare Analytics Database — SQL Practice

## Overview
SQL practice covering a relational healthcare schema and analysis of patients, doctors, appointments, bills, and departments.

## Files
- `healthcare_schema.sql` — schema-only version, without sample personal records and without a database-drop command.
- `healthcare_queries.sql` — reviewed example queries and a `vw_doctor_revenue` view.

## Run locally
Use a disposable MySQL 8 practice environment. Run `healthcare_schema.sql`, then run selected statements from `healthcare_queries.sql`. The tables remain empty until you add synthetic or otherwise authorized test data.

## Safety
The original LMS SQL file contains `DROP DATABASE IF EXISTS` and thousands of name/contact/address-like values. It has not been uploaded. The published schema-only version does not contain those sample records and does not drop a database.

## Validation status
The replacement schema and queries have been reviewed for structure. A MySQL server was not available here, so database execution and query results still require verification in MySQL 8.
