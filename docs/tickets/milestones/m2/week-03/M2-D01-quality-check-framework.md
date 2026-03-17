# Ticket: Implement explicit pass/fail quality framework

## Milestone
M2

## Day
D01

## Goal
Implement explicit pass/fail quality framework

## Context
This ticket is part of Week 03 progression for M2 local ETL learning.

## Tasks
- Read the ticket fully before implementation.
- Document your steps and assumptions in clear language.
- Keep outputs reproducible by another learner.
- Build on the Week 2 curated output instead of reading raw data directly.
- Place the quality-check code in `local/learning-workspace/m2/week-03/src/m2_etl/quality.py`.
- Implement explicit quality check functions with pass/fail status.
- Capture required columns, null thresholds, duplicates, and types.
- Start with the same issues already seen in M1 so the student can see the lineage from notebook checks to ETL checks.
- Produce a human-readable check summary.
- Save the summary note to `local/learning-workspace/m2/week-03/notes/d01-quality-framework.md`.

## Acceptance Criteria
- Quality checks can be run against the curated dataset produced in Week 2.
- Pass/fail output is readable enough to reference later in Week 4 logging and run summaries.
- The output note shows which checks passed, which failed, and where the curated input came from.
- Commands or outputs can be reproduced with documented steps.

## Verification
- Manual review of artifacts and notes.
- Re-run key commands and confirm expected outputs.

## Notes
Keep scope limited to this ticket and avoid jumping ahead.
## Supplemental Reading

- Docker Documentation: https://docs.docker.com/
- pandas Documentation: https://pandas.pydata.org/docs/
- Data validation (concept): https://en.wikipedia.org/wiki/Data_validation
