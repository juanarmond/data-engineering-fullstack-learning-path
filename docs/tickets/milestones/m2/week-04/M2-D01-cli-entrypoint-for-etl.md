# Ticket: Create cli entrypoint for etl execution

## Milestone
M2

## Day
D01

## Goal
Create CLI entrypoint for ETL execution

## Context
This ticket is part of Week 04 progression for M2 local ETL learning.

## Tasks
- Read the ticket fully before implementation.
- Document your steps and assumptions in clear language.
- Keep outputs reproducible by another learner.
- Create the CLI entrypoint in `local/learning-workspace/m2/week-04/src/m2_etl/cli.py` or equivalent.
- Make the CLI call the existing extract/transform/load flow from earlier M2 weeks instead of re-implementing the logic.
- Add single CLI command/entrypoint to run ETL.
- Document usage examples and expected outputs.
- Ensure command works from clean shell session.
- Document the main command in `local/learning-workspace/m2/week-04/notes/d01-cli-usage.md`.

## Acceptance Criteria
- One documented command runs the ETL path end-to-end from the repo root.
- The CLI delegates to earlier-stage code rather than duplicating ETL logic.
- Commands or outputs can be reproduced with documented steps.

## Verification
- Re-run the documented CLI command from a fresh shell session.
- Confirm the command writes output to the same curated location defined in Week 2.

## Notes
Keep scope limited to this ticket and avoid jumping ahead.
## Supplemental Reading

- Docker Documentation: https://docs.docker.com/
- pandas Documentation: https://pandas.pydata.org/docs/
- Data validation (concept): https://en.wikipedia.org/wiki/Data_validation
