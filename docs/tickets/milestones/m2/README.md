# Milestone M2: Local ETL Foundations and Reliability

## High-Level Objective
Transition from notebook-only analysis to a beginner-friendly local ETL workflow with clear contracts, quality checks, and repeatable execution.

## What You Will Achieve
By the end of M2, you should be able to:
- set up local tooling needed for ETL practice (including Docker basics),
- define ingestion-ready source and folder conventions,
- build a first local ETL flow (extract, transform, load),
- apply repeatable quality checks and basic modeled outputs,
- run ETL through a simple CLI-style workflow with tests and runbook notes.

## Weeks In This Milestone
- `week-01/` (setup foundations: Docker, local workspace, run readiness)
- `week-02/` (ETL foundations: extract/transform/load v1)
- `week-03/` (quality + modeling layer basics)
- `week-04/` (automation, reliability, and M3 handoff)

## Navigation

- Project README: [../../../../README.md](../../../../README.md)
- Roadmap: [../../../roadmap.md](../../../roadmap.md)
- Tickets guide: [../../README.md](../../README.md)

## How To Start
1. Confirm M1 Week 4 handoff notes are complete.
   - Reuse the dataset chosen in M1 Week 3 and documented in `local/learning-workspace/m1/week-04/notes/d07-m2-prep.md`.
   - `BRA.csv` is only a teacher example of one possible source file.
   - Reuse the M1 quality findings already documented in `local/learning-workspace/m1/week-03/notes/d05-quality-checks.md`.
   - Reuse the M1 readiness/handoff notes already documented in `local/learning-workspace/m1/week-03/notes/d07-weekly-review.md` and `local/learning-workspace/m1/week-04/notes/d07-m2-prep.md`.
2. Create milestone/week workspace folders:
   - `mkdir -p local/learning-workspace/m2/week-01`
   - `mkdir -p local/learning-workspace/m2/week-02`
   - `mkdir -p local/learning-workspace/m2/week-03`
   - `mkdir -p local/learning-workspace/m2/week-04`
3. Keep all M2 practice work inside `local/learning-workspace/m2/` so the student path stays separate from the course docs.
4. Use the same Python environment that was validated in M1.
   - Run `poetry install` once if dependencies are missing.
   - Use `poetry run python ...` and `poetry run black ...` for milestone commands so notebooks and CLI runs share the same environment.
   - If setup is flaky, run the verification guide before continuing: [docs/guides/setup-verification.md](../../../guides/setup-verification.md).
5. Complete `week-01/` setup tickets in order.
6. Continue with Week 2 -> Week 3 -> Week 4 in order.

## Expected Milestone Outputs

- Week 1 setup notes and Docker readiness checks.
- Week 2 ETL modules and curated outputs.
- Week 3 quality-check framework and modeled outputs.
- Week 4 CLI entrypoint, tests, runbook notes, and closeout handoff.

## Exit Criteria
You are ready for the next milestone when:
- local ETL runs end-to-end with documented commands,
- quality checks are explicit and repeatable,
- modeled outputs are documented and reviewable,
- runbook + handoff notes are clear for another contributor.
