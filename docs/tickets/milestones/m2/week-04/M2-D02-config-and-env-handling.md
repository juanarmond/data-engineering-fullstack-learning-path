# Ticket: Add config/env handling for paths and thresholds

## Milestone
M2

## Day
D02

## Goal
Add config/env handling for paths and thresholds

## Context
This ticket is part of Week 04 progression for M2 local ETL learning.

## Tasks
- Read the ticket fully before implementation.
- Document your steps and assumptions in clear language.
- Keep outputs reproducible by another learner.
- Add `.env.example` or a simple config module under `local/learning-workspace/m2/week-04/`.
- Keep the default paths aligned with the student workspace, especially the M1 raw source path and the M2 curated output path.
- Externalize key paths/thresholds to config or env vars.
- Provide defaults with clear override behavior.
- Document configuration contract.
- Save the configuration note to `local/learning-workspace/m2/week-04/notes/d02-config-contract.md`.

## Acceptance Criteria
- Configuration defaults let the ETL run in this repo without extra setup beyond the earlier milestones.
- Overrides are documented for learners who want to point at a copied raw file or different output folder.
- The note lists the default raw input path, modeled input path, and run artifact path.
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
