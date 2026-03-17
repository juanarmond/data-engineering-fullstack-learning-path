# Ticket: Exploratory Metrics and Data Profiling

## Milestone
M1

## Day
D04

## Goal
Compute baseline metrics to understand coverage and reliability of the data.

## Context
Before pipeline work, teams profile data to identify obvious quality and modeling risks.

## Tasks
- Compute row count and column count.
- Measure null counts/percentages per column.
- Check unique values for key identifiers (teams, match IDs if available).
- Assess date range and basic distribution for key numeric fields.
- Write a short summary of what looks healthy vs. risky in `local/learning-workspace/m1/week-03/notes/d04-profile-summary.md`.
- Keep profiling work inside a dedicated notebook section under a clear markdown heading.

## Acceptance Criteria
- Core profiling metrics are produced in the notebook.
- At least three data risks or caveats are identified.
- Findings are written in plain language.
- Profiling outputs appear in an explicitly labeled section.

## Verification
- Re-run notebook and confirm all profiling outputs are reproducible.
- Manual review of summary notes.

## Notes
Metrics should be simple and explainable, not exhaustive.
## Supplemental Reading

- pandas Documentation: https://pandas.pydata.org/docs/
- Jupyter Documentation: https://docs.jupyter.org/
- Python pathlib: https://docs.python.org/3/library/pathlib.html
