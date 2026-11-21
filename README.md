# Colombia Public Data Lakehouse

End-to-end data engineering project: automated extraction of Colombian public data
(TRM exchange rate, DANE population, minimum wage, inflation) into a Databricks
lakehouse using a Medallion architecture (Bronze → Silver → Gold), served through
BI dashboards and natural-language queries.

## Status
- [x] Day 1: first extraction from the datos.gov.co Socrata API (TRM)
- [ ] Week 1: pagination, retries, incremental loads, tests
- [ ] Week 2: DANE population, DIVIPOLA, Banco de la República sources
- [ ] Week 3+: Databricks Bronze / Silver / Gold, orchestration, Genie

## Tech stack
Python · requests · Git/GitHub · Databricks (Delta Lake, Unity Catalog) · dbt · GitHub Actions