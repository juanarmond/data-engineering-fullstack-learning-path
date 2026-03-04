# Week 01 Summary (M1 Data Foundations)

## Entry Criteria (Before Starting)

You should already have from M0:
- Git installed and working.
- Python and pip working from terminal.
- A cloned local copy of this repository.

Run these checks:
- `python --version`
- `python -m pip --version`
- `python -m pip install jupyter pandas`
- `python -m jupyter --version`

## Python-for-Data Micro Bridge

Before Day 1, make sure these concepts are clear:
- DataFrame and column operations.
- Data types (`int`, `float`, `string`, `datetime`).
- Missing values (nulls) and null rate.
- Filtering rows and selecting columns.

Starter links:
- pandas getting started: https://pandas.pydata.org/docs/getting_started/intro_tutorials/
- Jupyter docs: https://docs.jupyter.org/

## OS Command Note (Important)

Terminal commands can vary by OS (macOS, Linux, Windows). If a command in a ticket fails, you must research the equivalent command for your OS and document what you used in your notes.

## Weekly Plan (Time, Difficulty, Deliverables)

| Day | Ticket | Estimated Time | Difficulty | Required Deliverable |
|---|---|---|---|---|
| D01 | `M1-D01-data-source-selection-and-scope.md` | 60-90 min | Beginner | `docs/notes/m1/week-01/d01-source-scope.md` |
| D02 | `M1-D02-raw-data-download-and-storage-conventions.md` | 60-90 min | Beginner | Raw file(s) under `data/raw/` + `docs/notes/m1/week-01/d02-storage-conventions.md` |
| D03 | `M1-D03-first-jupyter-notebook-setup.md` | 90-120 min | Beginner | `notebooks/m1/week-01/m1_w1_d03_first_load.ipynb` |
| D04 | `M1-D04-exploratory-metrics-and-data-profiling.md` | 90-120 min | Beginner/Intermediate | Updated notebook profiling section + `docs/notes/m1/week-01/d04-profile-summary.md` |
| D05 | `M1-D05-data-quality-checks-v1.md` | 90-120 min | Intermediate | Updated notebook quality checks + `docs/notes/m1/week-01/d05-quality-checks.md` |
| D06 | `M1-D06-insights-summary-and-data-dictionary-draft.md` | 60-90 min | Beginner | `docs/notes/m1/week-01/d06-insights.md` + `docs/notes/m1/week-01/data-dictionary-draft.md` |
| D07 | `M1-D07-weekly-review-and-next-milestone-handoff.md` | 45-60 min | Beginner | `docs/notes/m1/week-01/d07-weekly-review.md` |

## Review Checkpoints

- Checkpoint A (after D03): notebook opens, data loads, columns are visible.
- Checkpoint B (after D05): profiling + quality outputs are reproducible.
- Checkpoint C (after D07): all week deliverables exist and are readable.

## Troubleshooting (By Theme)

- `ModuleNotFoundError: No module named 'pandas'` -> run `python -m pip install pandas`.
- `jupyter: command not found` -> run `python -m pip install jupyter` and start with `python -m jupyter notebook`.
- `FileNotFoundError` when loading CSV -> confirm your working directory with OS-equivalent command (`pwd` or alternative) and verify paths.
- If your shell or path commands differ from examples, research your OS-specific equivalent and add it to your notes.

## Exit Criteria (Definition of Done)

Week 1 is complete when:
- Dataset scope is documented.
- Raw files are stored using one naming convention.
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
- Prepare clear handoff notes for the next milestone.

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

- `M1-D01-data-source-selection-and-scope.md`
- `M1-D02-raw-data-download-and-storage-conventions.md`
- `M1-D03-first-jupyter-notebook-setup.md`
- `M1-D04-exploratory-metrics-and-data-profiling.md`
- `M1-D05-data-quality-checks-v1.md`
- `M1-D06-insights-summary-and-data-dictionary-draft.md`
- `M1-D07-weekly-review-and-next-milestone-handoff.md`
