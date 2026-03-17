# Week 04 Summary (M1 Notebook-Only Reproducible Analysis)

## Entry Criteria (Before Starting)

You should have from Week 3:
- A working notebook that loads and profiles the selected dataset.
- Initial quality checks and insights notes.
- A draft data dictionary.
- Week folder created: `local/learning-workspace/m1/week-04/`.
- Raw data stored at `local/learning-workspace/m1/data/raw/`.

Run these checks before Day 1:
- `ls -la local/learning-workspace/m1/week-03`
- `ls -la local/learning-workspace/m1/week-04`
- `poetry run python --version`
- `poetry run jupyter --version`
If your Python environment has changed since Week 3, re-verify setup first:
- [docs/guides/setup-verification.md](../../../../guides/setup-verification.md)
- `mkdir -p local/learning-workspace/m1/week-04/notebooks local/learning-workspace/m1/week-04/notes`

## OS Command Note (Important)

Command syntax and shell behavior vary by OS. If a command fails, research the correct command for your OS and document the equivalent in your run notes.

## Weekly Plan (Time, Difficulty, Deliverables)

| Day | Ticket | Estimated Time | Difficulty | Required Deliverable |
|---|---|---|---|---|
| D01 | [M1-D01-reproducibility-check-and-reset.md](M1-D01-reproducibility-check-and-reset.md) | 60-90 min | Beginner | `local/learning-workspace/m1/week-04/notebooks/m1_w4_analysis.ipynb` (reproducibility section) |
| D02 | [M1-D02-notebook-refactor-for-repeatability.md](M1-D02-notebook-refactor-for-repeatability.md) | 90-120 min | Intermediate | Same notebook (`local/learning-workspace/m1/week-04/notebooks/m1_w4_analysis.ipynb`) refactored with clean section structure |
| D03 | [M1-D03-profile-metrics-notebook-module.md](M1-D03-profile-metrics-notebook-module.md) | 90-120 min | Intermediate | Reusable profiling section in `local/learning-workspace/m1/week-04/notebooks/m1_w4_analysis.ipynb` |
| D04 | [M1-D04-quality-checks-notebook-module.md](M1-D04-quality-checks-notebook-module.md) | 90-120 min | Intermediate | Reusable quality-check section in `local/learning-workspace/m1/week-04/notebooks/m1_w4_analysis.ipynb` |
| D05 | [M1-D05-analysis-report-export-v1.md](M1-D05-analysis-report-export-v1.md) | 60-90 min | Intermediate | Notebook-generated report summary section (and optional export) |
| D06 | [M1-D06-confluence-runbook-and-troubleshooting.md](M1-D06-confluence-runbook-and-troubleshooting.md) | 60-90 min | Beginner/Intermediate | Notebook section plus `local/learning-workspace/m1/week-04/notes/d06-runbook.md` |
| D07 | [M1-D07-weekly-review-and-m2-prep.md](M1-D07-weekly-review-and-m2-prep.md) | 45-60 min | Beginner | `local/learning-workspace/m1/week-04/notes/d07-m2-prep.md` and notebook handoff section |

## Review Checkpoints

- Checkpoint A (after D02): notebook is readable and reproducible.
- Checkpoint B (after D04): profiling and quality sections are reusable and rerunnable.
- Checkpoint C (after D07): report, runbook notes, and M2 handoff files are complete and readable.

## Notebook Organization Rule (Mandatory)

All Week 4 notebook work must be organized with explicit markdown section headings.
Minimum required section flow:
- `Reproducibility`
- `Config`
- `Profile Metrics`
- `Quality Checks`
- `Report Summary`
- `Runbook/Troubleshooting`
- `Weekly Review/Handoff`

## Troubleshooting (By Theme)

- Notebook cannot find file -> check relative vs absolute path and current working directory.
- Different output between sections -> verify same source file and same filters.
- Import errors -> install missing package in the same environment used by notebook kernel.
- If command examples differ from your OS, research and document your equivalent command.

## Exit Criteria (Definition of Done)

Week 4 is complete when:
- Week 3 notebook work can be rerun from a clean state.
- Reusable profiling and quality-check sections exist in notebook form.
- A report summary is generated from notebook outputs.
- Notebook includes run instructions and troubleshooting notes.
- M2 prep notes are written in a reusable handoff file under `local/learning-workspace/m1/week-04/notes/`.

## What You Will Learn This Week

- Turn notebook exploration into repeatable notebook workflows.
- Re-run data checks on a fresh file without manual rework.
- Build reusable profiling and quality-check notebook sections.
- Produce a lightweight analysis report summary.
- Prepare clean notebook-based handoff inputs for ingestion automation work.

## Skills Focus

- Reproducible notebook workflow
- Reusable notebook design
- Repeatable data quality checks
- Analysis documentation quality
- Engineering handoff discipline

## Learning Resources

Official docs:
- pandas User Guide: https://pandas.pydata.org/docs/user_guide/index.html
- Jupyter Notebook docs: https://jupyter-notebook.readthedocs.io/
- JupyterLab docs: https://jupyterlab.readthedocs.io/en/stable/

Wikipedia (concept support):
- Reproducibility: https://en.wikipedia.org/wiki/Reproducibility
- Data profiling: https://en.wikipedia.org/wiki/Data_profiling
- Data validation: https://en.wikipedia.org/wiki/Data_validation

## Mandatory Tooling Requirement

Before completing Week 4, you must complete:
- [docs/guides/poetry-black-learning-track.md](../../../../guides/poetry-black-learning-track.md)

Recommended timing:
- During M0 Week 1, or before starting M1 Week 3 notebook work.

## Tickets in This Week

- [M1-D01-reproducibility-check-and-reset.md](M1-D01-reproducibility-check-and-reset.md)
- [M1-D02-notebook-refactor-for-repeatability.md](M1-D02-notebook-refactor-for-repeatability.md)
- [M1-D03-profile-metrics-notebook-module.md](M1-D03-profile-metrics-notebook-module.md)
- [M1-D04-quality-checks-notebook-module.md](M1-D04-quality-checks-notebook-module.md)
- [M1-D05-analysis-report-export-v1.md](M1-D05-analysis-report-export-v1.md)
- [M1-D06-confluence-runbook-and-troubleshooting.md](M1-D06-confluence-runbook-and-troubleshooting.md)
- [M1-D07-weekly-review-and-m2-prep.md](M1-D07-weekly-review-and-m2-prep.md)
