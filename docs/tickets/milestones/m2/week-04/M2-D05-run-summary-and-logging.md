# Ticket: Add run summary artifact and logging basics

## Milestone
M2

## Day
D05

## Goal
Add run summary artifact and logging basics

## Context
This ticket is part of Week 04 progression for M2 local ETL learning.

## Tasks
- Read the ticket fully before implementation.
- Document your steps and assumptions in clear language.
- Keep outputs reproducible by another learner.
- Write run artifacts under `local/learning-workspace/m2/week-04/runs/`.
- Include enough summary data to compare runs: input path, output path, row counts, check counts, timestamp, and final status.
- Add run summary output (rows processed/check status).
- Add basic structured logs for each ETL stage.
- Store run artifact in predictable location.
- Prefer a file such as `local/learning-workspace/m2/week-04/runs/latest-run-summary.json`.

## Acceptance Criteria
- Run summaries are stored in a documented location inside the student workspace.
- Logs make it easy to understand which stage failed without opening source files first.
- At least one concrete run-summary artifact exists after a successful run.
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
