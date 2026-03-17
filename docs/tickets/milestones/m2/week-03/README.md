# Week 03 Summary (M2 Quality and Modeling Basics)

## Entry Criteria (Before Starting)

- Week 2 ETL v1 flow runs end-to-end.
- Curated output files exist and are inspectable.

Run these checks before Day 1:
- `ls -la local/learning-workspace/m2/week-02/data/curated`
- `poetry run python --version`

## OS Command Note (Important)

Command syntax may vary across operating systems. If examples fail, use the OS-specific equivalent and document it in your work notes.

## What You Will Learn This Week

- Build repeatable quality-check framework.
- Enforce schema/type expectations.
- Create first modeled outputs for analytics use.
- Document assumptions in dictionary-style notes.

## Weekly Deliverables

- Quality-check framework with visible pass/fail outputs.
- Schema/type enforcement notes and examples.
- Null/duplicate handling strategy.
- Modeled outputs (`matches_clean`, `team_summary`).
- Updated model documentation and weekly readiness review.

## Repo-Specific Build Path

Use M2 Week 3 to extend the Week 2 ETL into a simple quality/modeling layer inside `local/learning-workspace/m2/week-03/`.

Recommended minimum layout:
- `local/learning-workspace/m2/week-03/src/m2_etl/quality.py`
- `local/learning-workspace/m2/week-03/src/m2_etl/models.py`
- `local/learning-workspace/m2/week-03/data/modeled/matches_clean.csv`
- `local/learning-workspace/m2/week-03/data/modeled/team_summary.csv`
- `local/learning-workspace/m2/week-03/notes/`

Expected source and output flow for this repo:
- source input: `local/learning-workspace/m2/week-02/data/curated/matches_curated.csv`
- quality output: readable pass/fail summary plus notes
- modeled outputs: `matches_clean.csv` and `team_summary.csv`
- documentation output: updated dictionary and weekly readiness note

## Review Checkpoints

- Checkpoint A (after D02): quality checks and schema expectations are visible.
- Checkpoint B (after D05): modeled outputs exist and can be explained in plain language.
- Checkpoint C (after D07): readiness for Week 4 automation is written down clearly.

## Skills Focus

- Data quality engineering
- Schema enforcement
- Modeling layer fundamentals
- Documentation quality

## Learning Resources

Official docs:
- Data validation (concept): https://en.wikipedia.org/wiki/Data_validation
- Data modeling (concept): https://en.wikipedia.org/wiki/Data_modeling
- DuckDB docs: https://duckdb.org/docs/

## Tickets in This Week

- [M2-D01-quality-check-framework.md](M2-D01-quality-check-framework.md)
- [M2-D02-schema-and-type-enforcement.md](M2-D02-schema-and-type-enforcement.md)
- [M2-D03-duplicate-and-null-handling-strategy.md](M2-D03-duplicate-and-null-handling-strategy.md)
- [M2-D04-modeled-output-matches-clean.md](M2-D04-modeled-output-matches-clean.md)
- [M2-D05-modeled-output-team-summary.md](M2-D05-modeled-output-team-summary.md)
- [M2-D06-model-documentation-and-dictionary.md](M2-D06-model-documentation-and-dictionary.md)
- [M2-D07-weekly-review-and-readiness-check.md](M2-D07-weekly-review-and-readiness-check.md)

## Exit Criteria (Definition of Done)

Week 3 is complete when:
- quality checks are repeatable and interpretable,
- modeled outputs are produced and documented,
- data assumptions and caveats are clearly recorded,
- readiness for automation week is confirmed.
