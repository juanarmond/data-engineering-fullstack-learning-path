# Ticket: Data Quality Checks v1

## Milestone
M1

## Day
D05

## Goal
Implement first manual data quality checks in notebook form.

## Context
Early quality checks establish a baseline and prepare for later scripted validation.

## Tasks
- Define simple checks (required columns, null thresholds, duplicates).
- Validate schema expectations (column presence and basic types).
- Identify rows failing each check.
- Record pass/fail status and example failing records.

## Acceptance Criteria
- At least three explicit data quality checks are implemented.
- Check outcomes are visible and interpretable.
- Failing examples are captured when applicable.

## Verification
- Re-run notebook and verify check results remain consistent.
- Manual review of pass/fail summary.

## Notes
Keep checks notebook-based for now; ingestion automation is introduced in M2.
