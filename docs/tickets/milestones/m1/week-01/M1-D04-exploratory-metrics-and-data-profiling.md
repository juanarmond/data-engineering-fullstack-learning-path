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
- Write a short summary of what looks healthy vs. risky.

## Acceptance Criteria
- Core profiling metrics are produced in the notebook.
- At least three data risks or caveats are identified.
- Findings are written in plain language.

## Verification
- Re-run notebook and confirm all profiling outputs are reproducible.
- Manual review of summary notes.

## Notes
Metrics should be simple and explainable, not exhaustive.
