# Ticket: Quality Checks Notebook Module

## Milestone
M1

## Day
D04

## Goal
Create reusable notebook cells/functions for first-pass data quality checks.

## Context
Repeatable notebook checks reduce manual errors while keeping the workflow beginner-friendly.

## What "Quality Checks" Means
Quality checks are simple rules to detect data problems early. For this ticket, quality checks are:
- required column check: confirm expected columns exist,
- null threshold check: flag columns with missing values above a chosen limit,
- duplicate check: detect duplicate rows (or duplicate key combinations),
- basic type check: verify key columns use expected types when possible.

## Tasks
- Add a dedicated quality-check section to the Week 4 notebook.
- Implement checks for required columns, null thresholds, duplicates, and basic types.
- Show pass/fail summary for each check.
- Display sample failing rows when checks fail.
- Ensure quality-check outputs are grouped under a clear markdown section heading.

## Expected Output Example
- `required_columns_check: PASS/FAIL`
- `null_threshold_check: PASS/FAIL` with flagged columns
- `duplicate_check: PASS/FAIL` with duplicate count
- `type_check: PASS/FAIL` with mismatched columns
- small table of failing examples when any check fails

## Acceptance Criteria
- Notebook includes reusable quality-check logic.
- Pass/fail outcomes are clearly visible.
- Failing examples are shown when applicable.
- All required checks listed above are implemented.

## Verification
- Restart kernel and run all cells.
- Confirm results align with Week 3 quality-check logic.

## OS and Research Note
Notebook and filesystem commands can vary by OS and shell. If a command fails, research the equivalent for your environment and document it.

## Notes
Keep this notebook-based; script extraction can happen in a later milestone.
## Supplemental Reading

- pandas Documentation: https://pandas.pydata.org/docs/
- Jupyter Documentation: https://docs.jupyter.org/
- Python pathlib: https://docs.python.org/3/library/pathlib.html
