# Ticket: M2 Preflight Readiness Check

## Milestone
M2

## Day
D03

## Goal
Run a fast readiness re-check before starting M2 ETL work.

## Context
Initial workspace, environment, and kernel setup is mandatory in M0.  
This ticket only confirms that setup is still working for M2 Week 1 and that the M1 handoff artifacts needed for ETL are still available.

## Tasks
- Confirm `local/learning-workspace/` exists.
- Confirm `local/learning-workspace/m2/week-01/` exists.
- Create notebook folder if missing: `mkdir -p local/learning-workspace/m2/week-01/notebooks`.
- Confirm the Week 4 handoff note clearly names the reused source file path for M2.
- Confirm that chosen source file actually exists.
- Confirm the M1 quality notes still exist: `local/learning-workspace/m1/week-03/notes/d05-quality-checks.md`.
- Verify Python environment is available.
- Verify formatting tooling from earlier milestones is still available.
- Verify Jupyter kernel is available.
- Verify Docker CLI is available for M2.

## Acceptance Criteria
- All preflight commands run successfully.
- M2 Week 1 workspace path exists and is ready for notebook/ETL files.
- The M1 dataset and handoff notes that feed M2 are present.
- The M1 handoff note is specific enough that M2 knows exactly which dataset to ingest.
- At least one usable local notebook kernel is available.
- Docker command works on the machine.

## Verification
- `ls -la local/learning-workspace`
- `ls -la local/learning-workspace/m2/week-01`
- `ls -la local/learning-workspace/m2/week-01/notebooks`
- `ls -la local/learning-workspace/m1/data/raw`
- `ls -la local/learning-workspace/m1/week-03/notes`
- `python --version`
- `poetry run python --version`
- `poetry run black --version`
- `jupyter kernelspec list`
- `docker --version`

## Notes
This is a re-check ticket, not a first-time setup ticket.
## Supplemental Reading

- Docker Documentation: https://docs.docker.com/
- pandas Documentation: https://pandas.pydata.org/docs/
- Data validation (concept): https://en.wikipedia.org/wiki/Data_validation
