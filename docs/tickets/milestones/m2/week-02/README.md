# Week 02 Summary (M2 ETL Foundations)

## Entry Criteria (Before Starting)

- Week 1 setup tickets completed.
- Docker and local Python workflow both functional.
- Shared dataset path and source assumptions documented.
- M1 handoff inputs available:
  - the learner's chosen dataset path documented in `local/learning-workspace/m1/week-04/notes/d07-m2-prep.md`
  - `local/learning-workspace/m1/week-03/notes/d05-quality-checks.md`
  - `local/learning-workspace/m1/week-04/notes/d07-m2-prep.md`
If setup is unstable, re-run the verification guide before Day 1:
- [docs/guides/setup-verification.md](../../../../guides/setup-verification.md)

Run these checks before Day 1:
- `ls -la local/learning-workspace/m2/week-02`
- `ls -la local/learning-workspace/m1/data/raw`
- `poetry run python --version`

## OS Command Note (Important)

Shell commands can vary by OS. If a command fails, find the equivalent command for your environment and record it in your notes.

## What You Will Learn This Week

- Define ETL scope and local architecture.
- Implement extract module from local raw files.
- Implement first transform rules from M1 findings.
- Load curated outputs to local files (CSV/Parquet).
- Document ETL run steps and verification evidence.

## Weekly Deliverables

- ETL scope and architecture notes.
- Raw/curated folder structure and data contract notes.
- Working extract/transform/load v1 flow.
- Curated output artifact(s) written locally.
- ETL runbook and weekly gap list.

## Skills Focus

- ETL basics
- File contracts
- Quality-rule translation
- Execution documentation

## Learning Resources

Official docs:
- Python pathlib: https://docs.python.org/3/library/pathlib.html
- pandas docs: https://pandas.pydata.org/docs/
- Apache Parquet: https://parquet.apache.org/docs/

## Repo-Specific Build Path

Use M2 Week 2 to create the first file-based ETL flow inside `local/learning-workspace/m2/week-02/`.

Recommended minimum layout:
- `local/learning-workspace/m2/week-02/src/m2_etl/extract.py`
- `local/learning-workspace/m2/week-02/src/m2_etl/transform.py`
- `local/learning-workspace/m2/week-02/src/m2_etl/load.py`
- `local/learning-workspace/m2/week-02/data/raw/`
- `local/learning-workspace/m2/week-02/data/interim/`
- `local/learning-workspace/m2/week-02/data/curated/`
- `local/learning-workspace/m2/week-02/notes/`

Expected source and output flow for this repo:
- source input: copy or reference the dataset recorded in the M1 Week 4 handoff note
- extract output: a DataFrame plus row/column summary in notes
- transform output: cleaned rows that apply M1 quality findings
- load output: deterministic `matches_curated.csv` and optional `matches_curated.parquet`

## Tickets in This Week

- [M2-D01-etl-scope-and-local-architecture.md](M2-D01-etl-scope-and-local-architecture.md)
- [M2-D02-folder-structure-and-data-contract.md](M2-D02-folder-structure-and-data-contract.md)
- [M2-D03-extract-module-local-files.md](M2-D03-extract-module-local-files.md)
- [M2-D04-transform-rules-v1.md](M2-D04-transform-rules-v1.md)
- [M2-D05-load-curated-output-v1.md](M2-D05-load-curated-output-v1.md)
- [M2-D06-etl-runbook-and-execution-notes.md](M2-D06-etl-runbook-and-execution-notes.md)
- [M2-D07-weekly-review-and-gap-list.md](M2-D07-weekly-review-and-gap-list.md)

## Review Checkpoints

- Checkpoint A (after D02): ETL folder layout and contract notes are in place.
- Checkpoint B (after D05): extract/transform/load v1 writes a stable curated output.
- Checkpoint C (after D07): runbook and gap list explain what Week 3 should improve.

## Exit Criteria (Definition of Done)

Week 2 is complete when:
- ETL v1 runs end-to-end on local data,
- transform rules are documented and repeatable,
- curated outputs are generated and reloadable,
- run instructions are clear to another learner.
