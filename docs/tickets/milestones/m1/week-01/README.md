# Week 01 Summary (M1 Python Basics for Data Work)

## Entry Criteria (Before Starting)

You should already have from M0:
- Git installed and working.
- Python and Poetry working from terminal.
- A cloned local copy of this repository.
- `local/learning-workspace/` created in repo root.
- Week folder created: `local/learning-workspace/m1/week-01/`.
- Dependencies installed from this repo's `pyproject.toml`.

Run these checks:
- `python --version`
- `poetry --version`
- `poetry run python --version`
- `poetry run jupyter --version`
- `jupyter kernelspec list`
- `ls -la local/learning-workspace/m1/week-01`
- `mkdir -p local/learning-workspace/m1/week-01/notebooks local/learning-workspace/m1/week-01/data local/learning-workspace/m1/week-01/notes`

## How To Start The Notebook

Choose one of these beginner-friendly options:
- Terminal/Jupyter: run `poetry run python -m jupyter notebook`, then create or open `local/learning-workspace/m1/week-01/notebooks/m1_w1_python_basics.ipynb`
- VS Code: create or open `local/learning-workspace/m1/week-01/notebooks/m1_w1_python_basics.ipynb`, then select the `Local Milestones (.venv)` kernel

Before you move past Day 1:
- restart the kernel,
- run the notebook cells from top to bottom,
- confirm the outputs appear without hidden manual steps.

## Why This Week Exists

This week is the programming bridge before SQL and later notebook analysis.
The goal is to make sure a beginner can:
- read and rerun notebook cells,
- change a variable and rerun the result,
- write a small function,
- loop through simple records,
- create a small dummy DataFrame that will be reused in Week 2 SQL work.

## OS Command Note (Important)

Terminal commands can vary by OS (macOS, Linux, Windows). If a command in a ticket fails, you must research the equivalent command for your OS and document what you used in your notes.

## Weekly Plan (Time, Difficulty, Deliverables)

| Day | Ticket | Estimated Time | Difficulty | Required Deliverable |
|---|---|---|---|---|
| D01 | [M1-D01-python-input-output-and-variables.md](M1-D01-python-input-output-and-variables.md) | 45-60 min | Beginner | `local/learning-workspace/m1/week-01/notebooks/m1_w1_python_basics.ipynb` (`Setup` + `Variables` sections) + `local/learning-workspace/m1/week-01/notes/d01-python-basics.md` |
| D02 | [M1-D02-lists-loops-and-conditionals.md](M1-D02-lists-loops-and-conditionals.md) | 60-90 min | Beginner | Same notebook (`Lists/Loops/If` section) + `local/learning-workspace/m1/week-01/notes/d02-loops.md` |
| D03 | [M1-D03-functions-and-small-reusable-code.md](M1-D03-functions-and-small-reusable-code.md) | 60-90 min | Beginner | Same notebook (`Functions` section) |
| D04 | [M1-D04-pathlib-and-local-files.md](M1-D04-pathlib-and-local-files.md) | 60-90 min | Beginner | Same notebook (`Dummy Dataset` section) + `local/learning-workspace/m1/week-01/notes/d04-paths.md` |
| D05 | [M1-D05-read-and-summarize-a-csv.md](M1-D05-read-and-summarize-a-csv.md) | 90-120 min | Beginner | Same notebook updated to export `local/learning-workspace/m1/week-01/data/dummy_matches.csv` + `local/learning-workspace/m1/week-01/notes/d05-csv-summary.md` |
| D06 | [M1-D06-mini-python-data-task.md](M1-D06-mini-python-data-task.md) | 90-120 min | Beginner/Intermediate | Same notebook (`Mini Task` section) + `local/learning-workspace/m1/week-01/notes/d06-mini-task.md` |
| D07 | [M1-D07-weekly-review-and-sql-readiness.md](M1-D07-weekly-review-and-sql-readiness.md) | 45-60 min | Beginner | `local/learning-workspace/m1/week-01/notes/d07-sql-readiness.md` |

## Review Checkpoints

- Checkpoint A (after D03): you can explain what a function input and output are.
- Checkpoint B (after D05): the notebook exports `dummy_matches.csv` and shows the DataFrame clearly.
- Checkpoint C (after D07): your notes clearly explain what you are ready to do in SQL next week.

## Notebook Organization Rule (Mandatory)

Use one notebook for the whole week:
- `local/learning-workspace/m1/week-01/notebooks/m1_w1_python_basics.ipynb`

Required section headings:
- `Setup`
- `Variables`
- `Lists/Loops/If`
- `Functions`
- `Dummy Dataset (DataFrame)`
- `Mini Task`
- `Weekly Review`

At the end of the week:
- restart the kernel,
- run all cells top to bottom,
- confirm `dummy_matches.csv` is regenerated without manual fixes.

## Troubleshooting (By Theme)

- `python: command not found` -> reopen terminal, confirm Python setup from M0, then retry.
- `FileNotFoundError` when loading CSV -> confirm your working directory with OS-equivalent command (`pwd` or alternative) and verify paths.
- DataFrame looks wrong -> print `df.head()` and `df.shape` after the cell that creates it.
- Notebook works only when cells are run out of order -> restart kernel and run all cells from the top.
- If your shell or path commands differ from examples, research your OS-specific equivalent and add it to your notes.

## Exit Criteria (Definition of Done)

Week 1 is complete when:
- one notebook runs top to bottom from a fresh kernel,
- you can explain variables, loops, functions, and file paths in plain language,
- the notebook creates and exports `local/learning-workspace/m1/week-01/data/dummy_matches.csv`,
- weekly review notes are complete and point to SQL as the next step.

## What You Will Learn This Week

- Use variables, lists, loops, and conditionals.
- Write simple functions with clear inputs/outputs.
- Read local files with `pathlib`.
- Create and inspect a small dummy DataFrame in Jupyter.
- Export that dataset to CSV so Week 2 can reuse it.
- Practice beginner debugging habits (print-based tracing and reading errors).
- Prepare clear handoff notes for SQL basics next week.

## Skills Focus

- Python syntax
- Small reusable functions
- File paths and local files
- Notebook workflow
- DataFrame basics
- CSV export literacy
- Beginner debugging habits
- Documentation and handoff habits

## Mini Glossary

- Variable: a named value in Python.
- Loop: repeat the same block for many values.
- Function: a reusable block of code with inputs and outputs.
- Path: the location of a file or folder.
- DataFrame: a table-like Python object with rows and columns.
- CSV: a text file with rows and columns separated by commas.

## Learning Resources

Official docs:
- Jupyter Documentation: https://docs.jupyter.org/
- Python `csv` module: https://docs.python.org/3/library/csv.html
- Python `pathlib` module: https://docs.python.org/3/library/pathlib.html
- pandas getting started: https://pandas.pydata.org/docs/getting_started/intro_tutorials/
- Python tutorial: https://docs.python.org/3/tutorial/

Wikipedia (concept support):
- CSV: https://en.wikipedia.org/wiki/Comma-separated_values

## Tickets in This Week

- [M1-D01-python-input-output-and-variables.md](M1-D01-python-input-output-and-variables.md)
- [M1-D02-lists-loops-and-conditionals.md](M1-D02-lists-loops-and-conditionals.md)
- [M1-D03-functions-and-small-reusable-code.md](M1-D03-functions-and-small-reusable-code.md)
- [M1-D04-pathlib-and-local-files.md](M1-D04-pathlib-and-local-files.md)
- [M1-D05-read-and-summarize-a-csv.md](M1-D05-read-and-summarize-a-csv.md)
- [M1-D06-mini-python-data-task.md](M1-D06-mini-python-data-task.md)
- [M1-D07-weekly-review-and-sql-readiness.md](M1-D07-weekly-review-and-sql-readiness.md)
