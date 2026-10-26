# Healthcare Analytics Database — SQL Practice

## Overview
A SQL practice project based on a relational healthcare database schema. The reviewed script defines tables for departments, doctors, patients, appointments, bills, and medications.

## Skills demonstrated by the project scope
- Relational table design and primary/foreign-key relationships
- Filtering records with WHERE conditions
- Aggregation and GROUP BY
- JOINs across doctors, departments, appointments, and billing records
- Views for reusable query results

## Example analysis tasks
- Find patients in a specified city
- Identify active doctors with more than ten years of experience
- Count patients or appointments by doctor
- Summarize paid bills by payment mode
- Rank departments by revenue
- Create a doctor-revenue view

## Important safety note
The source SQL script contains a `DROP DATABASE IF EXISTS` statement, which deletes an existing database with that name before recreating it. Review scripts carefully and run them only in a disposable practice environment. The source also contains names, contact fields, and email-like values; the raw SQL file has therefore **not** been published here pending a privacy and synthetic-data review.

## Project status
Documentation published; a sanitized schema, reviewed queries, and safe setup instructions still need to be prepared.
