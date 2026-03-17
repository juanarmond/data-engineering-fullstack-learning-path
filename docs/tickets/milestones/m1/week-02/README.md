# Week 02 Summary (M1 SQL Basics With Local Data)

## Entry Criteria (Before Starting)

You should have from Week 1:
- A Week 1 Python basics notebook that runs top to bottom.
- A Week 1 dummy dataset exported to CSV.
- Week 1 review notes completed.
- Week folder created: `local/learning-workspace/m1/week-02/`.

Run these checks before Day 1:
- `ls -la local/learning-workspace/m1/week-01`
- `ls -la local/learning-workspace/m1/week-02`
- `poetry run python --version`
- `poetry run python -c "import sqlite3; print(sqlite3.sqlite_version)"`
- `poetry run jupyter --version`
If your Python environment has changed since Week 1, re-verify setup first:
- [docs/guides/setup-verification.md](../../../../guides/setup-verification.md)
- `mkdir -p local/learning-workspace/m1/week-02/notebooks local/learning-workspace/m1/week-02/notes local/learning-workspace/m1/week-02/data`

## How To Start The Notebook

Choose one of these beginner-friendly options:
- Terminal/Jupyter: run `poetry run python -m jupyter notebook`, then create or open `local/learning-workspace/m1/week-02/notebooks/m1_w2_sql_basics.ipynb`
- VS Code: create or open `local/learning-workspace/m1/week-02/notebooks/m1_w2_sql_basics.ipynb`, then select the `Local Milestones (.venv)` kernel

Before you move past Day 1:
- restart the kernel,
- run the notebook cells from top to bottom,
- confirm the Week 1 CSV path can be read from inside the notebook.

## OS Command Note (Important)

Command syntax and shell behavior vary by OS. If a command fails, research the correct command for your OS and document the equivalent in your run notes.

## Weekly Plan (Time, Difficulty, Deliverables)

| Day | Ticket | Estimated Time | Difficulty | Required Deliverable |
|---|---|---|---|---|
| D01 | [M1-D01-what-sql-is-and-create-a-local-db.md](M1-D01-what-sql-is-and-create-a-local-db.md) | 45-60 min | Beginner | `local/learning-workspace/m1/week-02/notebooks/m1_w2_sql_basics.ipynb` (`Setup` section) + `local/learning-workspace/m1/week-02/notes/d01-sql-basics.md` |
| D02 | [M1-D02-load-csv-into-sqlite.md](M1-D02-load-csv-into-sqlite.md) | 60-90 min | Beginner | Same notebook (`Load Dataset` + `Create Table` sections) + `local/learning-workspace/m1/week-02/data/dummy_matches.db` + `local/learning-workspace/m1/week-02/notes/d02-load-plan.md` |
| D03 | [M1-D03-select-where-order-by.md](M1-D03-select-where-order-by.md) | 60-90 min | Beginner | Same notebook (`SELECT/WHERE/ORDER BY` section) + `local/learning-workspace/m1/week-02/notes/d03-query-results.md` |
| D04 | [M1-D04-group-by-and-aggregations.md](M1-D04-group-by-and-aggregations.md) | 60-90 min | Beginner | Same notebook (`GROUP BY` section) |
| D05 | [M1-D05-joins-and-compare-to-python-results.md](M1-D05-joins-and-compare-to-python-results.md) | 90-120 min | Beginner/Intermediate | Same notebook (`JOIN` section) + `local/learning-workspace/m1/week-02/notes/d05-sql-vs-python.md` |
| D06 | [M1-D06-quality-queries-and-null-checks.md](M1-D06-quality-queries-and-null-checks.md) | 90-120 min | Beginner/Intermediate | Same notebook (`Quality Queries` section) + `local/learning-workspace/m1/week-02/notes/d06-quality-queries.md` |
| D07 | [M1-D07-weekly-review-and-notebook-readiness.md](M1-D07-weekly-review-and-notebook-readiness.md) | 45-60 min | Beginner | `local/learning-workspace/m1/week-02/notes/d07-notebook-readiness.md` |

## Review Checkpoints

- Checkpoint A (after D02): you understand what table, row, and column mean in SQL.
- Checkpoint B (after D04): you can write one `GROUP BY` query and explain the result.
- Checkpoint C (after D07): your notes explain how SQL helped you understand the same dataset you created in Week 1 before notebook analysis starts.

## Notebook Organization Rule (Mandatory)

Use one notebook for the whole week:
- `local/learning-workspace/m1/week-02/notebooks/m1_w2_sql_basics.ipynb`

Required section headings:
- `Setup`
- `Load Dataset`
- `Create Table`
- `SELECT/WHERE/ORDER BY`
- `GROUP BY`
- `JOIN`
- `Quality Queries`
- `Weekly Review / Notebook Readiness`

Important:
- write visible SQL in notebook cells or Python strings,
- keep the SQL text readable,
- restart kernel and run all cells before calling the week complete.

## Troubleshooting (By Theme)

- `no such table` -> confirm the table was created and loaded before running the query.
- Wrong row count -> re-check filters, `WHERE` conditions, and duplicates in the source file.
- SQL output differs from Python summary -> compare the exact grouping keys and filters used in both places.
- Week 2 cannot find the CSV from Week 1 -> confirm `local/learning-workspace/m1/week-01/data/dummy_matches.csv` exists and rerun the Week 1 export cell if needed.
- If command examples differ from your OS, research and document your equivalent command.

## Exit Criteria (Definition of Done)

Week 2 is complete when:
- you can explain `SELECT`, `WHERE`, `GROUP BY`, and `JOIN`,
- one notebook runs top to bottom from a fresh kernel,
- the notebook loads the Week 1 CSV and creates `dummy_matches.db`,
- at least one quality-focused SQL query exists in the notebook,
- your notes explain how SQL work prepares you for notebook analysis next week.

## What You Will Learn This Week

- Understand what SQL is good at.
- Load the Week 1 dummy dataset into a simple local database.
- Write beginner queries to filter, sort, group, and join the same dataset.
- Use SQL for simple data quality checks before deeper analysis.
- Prepare for notebook-based profiling next week (Week 3).

## Skills Focus

- SQL syntax
- Local database basics
- Query reading and interpretation
- Notebook SQL workflow
- Data quality questioning
- Analysis preparation habits

## Learning Resources

Official docs:
- Python `sqlite3` module: https://docs.python.org/3/library/sqlite3.html
- SQLBolt: https://sqlbolt.com/
- SQLite docs: https://www.sqlite.org/docs.html

Wikipedia (concept support):
- SQL: https://en.wikipedia.org/wiki/SQL
- SQLite: https://en.wikipedia.org/wiki/SQLite
- Join (SQL): https://en.wikipedia.org/wiki/Join_(SQL)

## Self-Check Questions

- Can I explain what problem SQL solves better than manual spreadsheet filtering?
- Can I tell the difference between a raw row count and a grouped summary?
- Can I explain why a null check query might matter before notebook work starts?
- Can I explain how Week 2 continues the same dataset story from Week 1?

## Tickets in This Week

- [M1-D01-what-sql-is-and-create-a-local-db.md](M1-D01-what-sql-is-and-create-a-local-db.md)
- [M1-D02-load-csv-into-sqlite.md](M1-D02-load-csv-into-sqlite.md)
- [M1-D03-select-where-order-by.md](M1-D03-select-where-order-by.md)
- [M1-D04-group-by-and-aggregations.md](M1-D04-group-by-and-aggregations.md)
- [M1-D05-joins-and-compare-to-python-results.md](M1-D05-joins-and-compare-to-python-results.md)
- [M1-D06-quality-queries-and-null-checks.md](M1-D06-quality-queries-and-null-checks.md)
- [M1-D07-weekly-review-and-notebook-readiness.md](M1-D07-weekly-review-and-notebook-readiness.md)
