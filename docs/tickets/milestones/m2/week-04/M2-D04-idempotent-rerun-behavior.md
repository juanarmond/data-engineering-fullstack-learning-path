# Ticket: Guarantee safe reruns and deterministic outputs

## Milestone
M2

## Day
D04

## Goal
Guarantee safe reruns and deterministic outputs

## Context
This ticket is part of Week 04 progression for M2 local ETL learning.

## Tasks
- Read the ticket fully before implementation.
- Document your steps and assumptions in clear language.
- Keep outputs reproducible by another learner.
- Ensure rerunning ETL does not corrupt outputs.
- Define overwrite/append policy explicitly.
- Verify deterministic rerun behavior.
- Save the rerun note to `local/learning-workspace/m2/week-04/notes/d04-rerun-policy.md`.

## Acceptance Criteria
- Deliverable is complete and understandable by a beginner reviewer.
- The note explains what happens when outputs already exist and how a learner can verify a safe rerun.
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
