# Portfolio Audit and Completion Tracker

**Last reviewed:** 27 October 2026  
**Scope:** Public portfolio repository and the project files/workflows listed below.

This tracker separates checks that have passed from tasks that require manual software or source-data review. A green automated check is evidence for the tested behavior only; it is not a blanket certification of every project.

## Verified automated checks

| Project / check | Evidence | Status and limits |
|---|---|---|
| Supply Chain & Inventory Analytics | [Latest passing workflow](https://github.com/3ankitrathod-hash/3ankitrathod-hash/actions/runs/40505325575) | Python analysis, output-file checks, MySQL 8 SQL execution, overall KPI comparison, and Python/MySQL reorder-alert comparison passed on synthetic data. |
| Healthcare Analytics SQL | [Passing workflow](https://github.com/3ankitrathod-hash/3ankitrathod-hash/actions/runs/40503139615) | Schema, fictional seed data, reporting queries, and doctor revenue view passed on fictional records. |
| Global Trade Data Analysis | [Passing workflow](https://github.com/3ankitrathod-hash/3ankitrathod-hash/actions/runs/40502858665) | Workbook opens and KPI summary arithmetic checks pass. This does not independently validate every workbook formula or reconcile raw rows. |
| Notebook demo projects | [Passing workflow](https://github.com/3ankitrathod-hash/3ankitrathod-hash/actions/runs/40502700313) | Olympic, customer feedback, and employee wellness notebooks execute in synthetic/demo mode. This does not validate the original datasets or real-world conclusions. |
| Space Mission Analysis | [Latest passing demo check](https://github.com/3ankitrathod-hash/3ankitrathod-hash/actions/runs/40505429522) | Analysis script executes on the included synthetic demonstration CSV. Do not present its output as historical space-industry findings. |
| Portfolio documentation | [Portfolio Integrity workflow](https://github.com/3ankitrathod-hash/3ankitrathod-hash/actions/workflows/portfolio-integrity-check.yml) | Local README links and required project documentation are checked automatically. |
| General CI and security | [GitHub Actions](https://github.com/3ankitrathod-hash/3ankitrathod-hash/actions) | Check individual latest runs for the final status; older passing runs do not guarantee a later commit is clean. |

## Changes made during this review

1. Removed the already-completed SQL/Python KPI comparison from the Supply Chain README's outstanding-task list.
2. Updated the MySQL inventory reorder query to choose the latest record per SKU and warehouse before evaluating the reorder point.
3. Extended the Supply Chain GitHub Actions workflow to compare SQL reorder candidates against Python's generated alert CSV. The workflow passed.
4. Corrected the Space Mission script's missing-dataset error text to acknowledge that the repository includes a synthetic demo dataset.

## Remaining work that needs a human or additional evidence

- [ ] **Power BI:** Open Power BI Desktop, import the Supply Chain CSVs, build the specified report, compare KPI cards and charts with CSV outputs, and save the actual PBIX file. Add genuine screenshots only after visual review. The DAX file and guide are not a PBIX.
- [ ] **Global Trade:** Manually reconcile workbook formulas and summary figures to the underlying raw/clean sheets; check pivot tables and formatting.
- [ ] **Datasets:** Confirm provenance and redistribution permissions for each dataset. Keep fictional/demo results clearly labelled and do not publish identifiable health, workplace, or customer data.
- [ ] **Social Media SQL:** Check the latest MySQL 8 workflow result and inspect result sets; the existence of a workflow file alone is not proof that it passed.
- [ ] **Career presentation:** Update resume/LinkedIn project bullets only with skills and results that can be demonstrated from the actual code, query outputs, and dashboard.

## Synthetic data and metric integrity

The Supply Chain snapshot documents 120 synthetic order rows, 1,620 units, 140,275.80 in unspecified demo currency units of sales, 87,500.24 estimated cost, 52,775.56 estimated gross profit, and 37.62% estimated gross margin. These are illustrative sample calculations, not actual employer or customer results.

Healthcare and social-media seed records are fictional. The small Olympic, customer-feedback, employee-wellness, and space-mission demo datasets must not be presented as full original datasets or as evidence of real-world trends.

## Definition of complete

A project is ready to showcase only when:
1. A new user can follow its README and reproduce the result.
2. Required data files are included or the data source and license are documented.
3. Code/queries execute successfully in the stated environment.
4. Key outputs are checked against independent calculations or expected results.
5. Limitations, synthetic data, and assumptions are explicit.
6. Screenshots and dashboard files are genuine and match the committed analysis.