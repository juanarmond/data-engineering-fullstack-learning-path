# Week 04 Summary (M2 Automation and Reliability)

## Entry Criteria (Before Starting)

- Week 3 quality and modeled outputs complete.
- ETL code is understandable and runnable manually.
- The student already has a working Week 2/3 code path inside `local/learning-workspace/m2/`.

Run these checks before Day 1:
- `ls -la local/learning-workspace/m2/week-04`
- `poetry run python --version`

## OS Command Note (Important)

CLI, test, and logging commands can differ by OS and shell. If a command fails, use your OS-equivalent command and document it.

## What You Will Learn This Week

- Add CLI-style entrypoint for ETL run.
- Add config/env handling and idempotent reruns.
- Add baseline tests for extract/transform/load.
- Create final operational runbook and M3 handoff.

## Weekly Deliverables

- CLI entrypoint for ETL execution.
- Config/env handling for repeatable runs.
- Baseline automated tests.
- Idempotent rerun behavior documented.
- Run summary/log output and final Confluence-style runbook.
- M2 closeout and M3 handoff priorities.

## Review Checkpoints

- Checkpoint A (after D02): CLI path and config story are documented.
- Checkpoint B (after D04): tests and rerun behavior are working or explicitly blocked.
- Checkpoint C (after D07): closeout notes explain what the next milestone should build on.

## Skills Focus

- Automation basics
- Reliability patterns
- Testing
- Operational handoff

## Learning Resources

Official docs:
- unittest docs: https://docs.python.org/3/library/unittest.html
- Python argparse: https://docs.python.org/3/library/argparse.html
- Logging HOWTO: https://docs.python.org/3/howto/logging.html

## Repo-Specific Build Path

Week 4 should wrap the Week 2 and Week 3 work, not replace it.

Recommended minimum additions:
- `local/learning-workspace/m2/week-04/src/m2_etl/cli.py`
- `local/learning-workspace/m2/week-04/tests/`
- `local/learning-workspace/m2/week-04/.env.example`
- `local/learning-workspace/m2/week-04/runs/`
- `local/learning-workspace/m2/week-04/notes/d06-final-runbook.md`
- `local/learning-workspace/m2/week-04/notes/d07-m3-handoff.md`

The Week 4 command path should still use the student workspace under `local/learning-workspace/m2/` and should call into the ETL stages already built in earlier weeks.

## Tickets in This Week

- [M2-D01-cli-entrypoint-for-etl.md](M2-D01-cli-entrypoint-for-etl.md)
- [M2-D02-config-and-env-handling.md](M2-D02-config-and-env-handling.md)
- [M2-D03-tests-for-etl-basics.md](M2-D03-tests-for-etl-basics.md)
- [M2-D04-idempotent-rerun-behavior.md](M2-D04-idempotent-rerun-behavior.md)
- [M2-D05-run-summary-and-logging.md](M2-D05-run-summary-and-logging.md)
- [M2-D06-final-runbook-confluence-style.md](M2-D06-final-runbook-confluence-style.md)
- [M2-D07-m2-closeout-and-m3-handoff.md](M2-D07-m2-closeout-and-m3-handoff.md)

## Exit Criteria (Definition of Done)

Week 4 is complete when:
- ETL can be triggered through a single documented command path,
- tests run and validate core ETL behavior,
- reruns are deterministic and safe,
- final runbook and handoff notes are complete.
