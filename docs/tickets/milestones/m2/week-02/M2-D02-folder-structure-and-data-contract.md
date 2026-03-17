# Ticket: Create folder layout and raw/curated contract

## Milestone
M2

## Day
D02

## Goal
Create folder layout and raw/curated contract

## Context
This ticket is part of Week 02 progression for M2 local ETL learning.

## Tasks
- Read the ticket fully before implementation.
- Document your steps and assumptions in clear language.
- Keep outputs reproducible by another learner.
- Create the Week 2 working folders inside `local/learning-workspace/m2/week-02/`:
  - `src/m2_etl/`
  - `data/raw/`
  - `data/interim/`
  - `data/curated/`
  - `notes/`
- Decide whether the dataset named in `local/learning-workspace/m1/week-04/notes/d07-m2-prep.md` will be copied into `data/raw/` or referenced in place, and document that choice.
- Create/confirm raw, interim, and curated folder conventions.
- Define naming rules for files and run artifacts.
- Document data contract expectations for the key fields carried from your chosen M1 dataset and handoff note.
- Save the contract note to `local/learning-workspace/m2/week-02/notes/d02-data-contract.md`.

## Acceptance Criteria
- Folder layout exists under `local/learning-workspace/m2/week-02/`.
- Contract notes explain where source data comes from and where curated outputs will be written.
- Commands or outputs can be reproduced with documented steps.

## Verification
- `find local/learning-workspace/m2/week-02 -maxdepth 3 | sort`
- Open `local/learning-workspace/m2/week-02/notes/d02-data-contract.md`.

## Notes
Keep scope limited to this ticket and avoid jumping ahead.
## Supplemental Reading

- Docker Documentation: https://docs.docker.com/
- pandas Documentation: https://pandas.pydata.org/docs/
- Data validation (concept): https://en.wikipedia.org/wiki/Data_validation
