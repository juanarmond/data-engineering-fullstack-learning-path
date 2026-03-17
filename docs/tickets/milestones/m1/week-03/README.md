# Week 03 Summary (M1 Data Foundations)

## Entry Criteria (Before Starting)

You should already have completed:
- M1 Week 1 (Python basics) and Week 2 (SQL basics).

You should also already have from M0:
- Git installed and working.
- Python and Poetry working from terminal.
- A cloned local copy of this repository.
- `local/learning-workspace/` created in repo root.
- Week folder created: `local/learning-workspace/m1/week-03/`.
- Dependencies installed from this repo's `pyproject.toml`.

Run these checks:
- `python --version`
- `poetry --version`
- `poetry run python --version`
- `poetry run jupyter --version`
- `jupyter kernelspec list`
- `ls -la local/learning-workspace/m1/week-03`
- `mkdir -p local/learning-workspace/m1/data/raw local/learning-workspace/m1/week-03/notebooks local/learning-workspace/m1/week-03/notes`

## Prior Learning Reminder

Before Day 1, confirm you can already do these basics from M1 Week 1 and Week 2:
- assign variables and call functions,
- loop through a small list of records,
- open a CSV file path with `pathlib`,
- explain a simple `SELECT ... WHERE ... GROUP BY ...` query in plain language.

## OS Command Note (Important)

Terminal commands can vary by OS (macOS, Linux, Windows). If a command in a ticket fails, you must research the equivalent command for your OS and document what you used in your notes.

## Weekly Plan (Time, Difficulty, Deliverables)

| Day | Ticket | Estimated Time | Difficulty | Required Deliverable |
|---|---|---|---|---|
| D01 | [M1-D01-data-source-selection-and-scope.md](M1-D01-data-source-selection-and-scope.md) | 60-90 min | Beginner | `local/learning-workspace/m1/week-03/notes/d01-source-scope.md` |
| D02 | [M1-D02-raw-data-download-and-storage-conventions.md](M1-D02-raw-data-download-and-storage-conventions.md) | 60-90 min | Beginner | Raw file(s) under `local/learning-workspace/m1/data/raw/` + `local/learning-workspace/m1/week-03/notes/d02-storage-conventions.md` |
| D03 | [M1-D03-first-jupyter-notebook-setup.md](M1-D03-first-jupyter-notebook-setup.md) | 90-120 min | Beginner | `local/learning-workspace/m1/week-03/notebooks/m1_w3_analysis.ipynb` |
| D04 | [M1-D04-exploratory-metrics-and-data-profiling.md](M1-D04-exploratory-metrics-and-data-profiling.md) | 90-120 min | Beginner/Intermediate | Updated profiling section in `local/learning-workspace/m1/week-03/notebooks/m1_w3_analysis.ipynb` + `local/learning-workspace/m1/week-03/notes/d04-profile-summary.md` |
| D05 | [M1-D05-data-quality-checks-v1.md](M1-D05-data-quality-checks-v1.md) | 90-120 min | Intermediate | Updated quality checks in `local/learning-workspace/m1/week-03/notebooks/m1_w3_analysis.ipynb` + `local/learning-workspace/m1/week-03/notes/d05-quality-checks.md` |
| D06 | [M1-D06-insights-summary-and-data-dictionary-draft.md](M1-D06-insights-summary-and-data-dictionary-draft.md) | 60-90 min | Beginner | `local/learning-workspace/m1/week-03/notes/d06-insights.md` + `local/learning-workspace/m1/week-03/notes/data-dictionary-draft.md` |
| D07 | [M1-D07-weekly-review-and-next-milestone-handoff.md](M1-D07-weekly-review-and-next-milestone-handoff.md) | 45-60 min | Beginner | `local/learning-workspace/m1/week-03/notes/d07-weekly-review.md` |

## Review Checkpoints

- Checkpoint A (after D03): notebook opens, data loads, columns are visible.
- Checkpoint B (after D05): profiling + quality outputs are reproducible.
- Checkpoint C (after D07): all week deliverables exist and are readable.

## Notebook Organization Rule (Mandatory)

For every notebook created or updated in this week, use clear markdown section headings.
Minimum section pattern:
- `Load`
- `Profile`
- `Quality Checks`
- `Insights/Notes`

## Troubleshooting (By Theme)

- `ModuleNotFoundError: No module named 'pandas'` -> run `poetry install` and then retry with `poetry run python ...`.
- `jupyter: command not found` -> run `poetry install` and start with `poetry run python -m jupyter notebook`.
- `FileNotFoundError` when loading CSV -> confirm your working directory with OS-equivalent command (`pwd` or alternative) and verify paths.
- If your shell or path commands differ from examples, research your OS-specific equivalent and add it to your notes.

## Exit Criteria (Definition of Done)

Week 3 is complete when:
- Dataset scope is documented.
- Raw files are stored under `local/learning-workspace/m1/data/raw/` using one naming convention.
- Notebook runs from top to bottom from a clean kernel.
- Profiling metrics and quality checks are present.
- Insights summary and draft data dictionary are written.
- Weekly review/handoff note is completed.

## What You Will Learn This Week

- Choose and scope an initial public dataset.
- Download and organize raw files with clear naming conventions.
- Set up a first Jupyter notebook for exploratory analysis.
- Compute baseline metrics to understand data quality and coverage.
- Run basic manual data quality checks.
- Document early insights and a first data dictionary draft.
- Prepare clear handoff notes for Week 4 reproducibility work.

## Skills Focus

- Data source scoping
- Raw data organization
- Jupyter notebook workflow
- Exploratory data analysis (EDA)
- Basic data quality validation
- Documentation and handoff habits

## Mini Glossary

- Schema: the expected set of columns and data types.
- Null rate: percentage of missing values in a column.
- Duplicate row: repeated record that should likely appear once.
- Key identifier: column(s) used to uniquely identify a record.
- Distribution: how values are spread (for example min/max/frequency).

## Learning Resources

Official docs:
- Jupyter Documentation: https://docs.jupyter.org/
- pandas Documentation: https://pandas.pydata.org/docs/
- Python `csv` module: https://docs.python.org/3/library/csv.html
- Python `pathlib` module: https://docs.python.org/3/library/pathlib.html

Wikipedia (concept support):
- Exploratory data analysis: https://en.wikipedia.org/wiki/Exploratory_data_analysis
- Data quality: https://en.wikipedia.org/wiki/Data_quality
- CSV: https://en.wikipedia.org/wiki/Comma-separated_values

## Tickets in This Week

- [M1-D01-data-source-selection-and-scope.md](M1-D01-data-source-selection-and-scope.md)
- [M1-D02-raw-data-download-and-storage-conventions.md](M1-D02-raw-data-download-and-storage-conventions.md)
- [M1-D03-first-jupyter-notebook-setup.md](M1-D03-first-jupyter-notebook-setup.md)
- [M1-D04-exploratory-metrics-and-data-profiling.md](M1-D04-exploratory-metrics-and-data-profiling.md)
- [M1-D05-data-quality-checks-v1.md](M1-D05-data-quality-checks-v1.md)
- [M1-D06-insights-summary-and-data-dictionary-draft.md](M1-D06-insights-summary-and-data-dictionary-draft.md)
- [M1-D07-weekly-review-and-next-milestone-handoff.md](M1-D07-weekly-review-and-next-milestone-handoff.md)
