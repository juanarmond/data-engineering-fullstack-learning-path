# Ticket: Profile Metrics Notebook Module

## Milestone
M1

## Day
D03

## Goal
Create reusable notebook cells/functions that reproduce core profiling metrics.

## Context
Keeping repeated profiling logic inside a notebook helps beginners stay in one tool while still improving repeatability.

## What "Profile Metrics" Means
Profile metrics are simple numbers that describe the dataset shape and completeness before any modeling or automation. For this ticket, profile metrics are:
- total rows (how many records),
- total columns (how many fields),
- column names (what fields exist),
- null count and null rate per column (how much data is missing),
- date coverage (earliest and latest date, if a date column exists),
- unique count for key columns (for example team names).

## Tasks
- Add a dedicated profiling section to the Week 2 notebook.
- Build reusable notebook cells/functions for row/column count, null percentages, date range, and key unique counts.
- Parameterize key values in a config cell (for example input path and key columns).
- Validate profiling outputs against Week 1 results.
- Ensure profiling section has a clear markdown title so outputs are easy to locate.

## Expected Output Example
- `row_count = ...`
- `column_count = ...`
- table with `column`, `null_count`, `null_rate_pct`
- `min_date` and `max_date` (if available)
- `n_unique_home_team`, `n_unique_away_team` (or equivalent key fields)

## Acceptance Criteria
- Notebook includes reusable profiling logic in one clear section.
- Profiling outputs are rerunnable and consistent.
- Config values are centralized in the notebook.
- All required profile metrics listed above are visible in output.

## Verification
- Restart kernel and run all cells.
- Confirm profiling outputs match expected values from Week 1.

## OS and Research Note
Python and notebook launch commands can vary by OS. If examples fail, research the equivalent command for your OS and document what you used.

## Notes
Keep implementation in notebook form only for this week.
## Supplemental Reading

- pandas Documentation: https://pandas.pydata.org/docs/
- Jupyter Documentation: https://docs.jupyter.org/
- Python pathlib: https://docs.python.org/3/library/pathlib.html

