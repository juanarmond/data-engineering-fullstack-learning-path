# Data Engineering and Full-Stack Learning Path

A guided project for learning by building.

This repository is designed for learners who want practical, job-relevant experience across data engineering and full-stack delivery, but need a clear sequence instead of random tutorials.

## Project Introduction

This is not a clone-and-run template.

It is a structured learning journey where you:
- set up your engineering environment,
- collect and understand real data,
- build repeatable analysis habits,
- prepare ingestion/automation foundations,
- and progress toward API and dashboard implementation.

The structure mirrors real team workflow: small scoped tasks, explicit deliverables, and weekly handoffs.

## Start Here (5 Minutes)

1. Read [docs/roadmap.md](docs/roadmap.md).
2. Read [docs/tickets/README.md](docs/tickets/README.md).
3. Create your first local workspace folder:
   - `mkdir -p local/learning-workspace/m0/week-01`
4. Open [docs/tickets/milestones/m0/README.md](docs/tickets/milestones/m0/README.md).
5. Continue to [docs/tickets/milestones/m0/week-01/README.md](docs/tickets/milestones/m0/week-01/README.md) and complete Day 1 first.

## Project Goal

Build an end-to-end portfolio project while learning core engineering behaviors:
- planning before implementation,
- writing reproducible work,
- validating data quality,
- documenting decisions,
- and shipping incrementally.

By the end of the full path, you should be able to explain both your technical choices and your delivery process.

## By The End Of This Path

- `M0`: a working local setup, a repeatable Python toolchain, and a first branch/commit/PR workflow.
- `M1`: Python basics, SQL basics, a reproducible notebook workflow, stored raw data, profiling notes, quality-check notes, and handoff notes.
- `M2`: a local ETL workflow with extract/transform/load stages, quality checks, modeled outputs, tests, and runbook notes.
- Later milestones: API, dashboard, and deployment work built on top of the earlier data workflow.

## Canonical Learning Path

Use this path in order:
1. [docs/roadmap.md](docs/roadmap.md)
2. [docs/tickets/README.md](docs/tickets/README.md)
3. [docs/tickets/milestones/m0/README.md](docs/tickets/milestones/m0/README.md)
4. [docs/tickets/milestones/m1/README.md](docs/tickets/milestones/m1/README.md)
5. [docs/tickets/milestones/m2/README.md](docs/tickets/milestones/m2/README.md)

Then follow each milestone's week/day tickets in sequence.

## Where Your Work Lives

- Learner outputs should live under `local/learning-workspace/`.
- That folder is gitignored by design so you can practice safely without polluting the course docs.
- Repository docs and ticket files stay in `docs/` and are the part you would normally review or update in git.

## Current Scope

- `M0` onboarding fundamentals
- `M1` Python basics, SQL basics, and reproducible notebook analysis
- `M2` local ETL foundations and reliability (week-01 to week-04)

## Mandatory Tooling Standard

All learners must complete the Poetry + Black setup using the tracked project configuration in `pyproject.toml`:
- [docs/guides/poetry-black-learning-track.md](docs/guides/poetry-black-learning-track.md)

This is a required part of the learning path and is validated during milestone checks.
Use `poetry ...` and `poetry run ...` as the canonical command style across this repo.
If `poetry` is not found on your machine, follow the OS-specific setup verification steps in:
- [docs/guides/setup-verification.md](docs/guides/setup-verification.md)

Note: `poetry.lock` is committed to this repo on purpose so installs are reproducible across learners and machines.

## Guides

Practical command references are available in:
- [docs/guides/README.md](docs/guides/README.md)

## Milestones

- `M0`: [docs/tickets/milestones/m0/README.md](docs/tickets/milestones/m0/README.md)
- `M1`: [docs/tickets/milestones/m1/README.md](docs/tickets/milestones/m1/README.md)
- `M2`: [docs/tickets/milestones/m2/README.md](docs/tickets/milestones/m2/README.md)

## Free Data Sources

Always verify license, attribution, and usage terms before using a source.

Football/sports-friendly options:
- Football-Data (CSV historical results): https://www.football-data.co.uk/data.php
- football-data.org (free API tier available): https://www.football-data.org/
- FiveThirtyEight datasets (public GitHub repo): https://github.com/fivethirtyeight/data

General open data sources:
- World Bank Open Data: https://data.worldbank.org/
- Our World in Data datasets: https://ourworldindata.org/data
- U.S. Data.gov portal: https://www.data.gov/
- EU Open Data portal: https://data.europa.eu/
- UCI Machine Learning Repository: https://archive.ics.uci.edu/
- Kaggle public datasets (free account): https://www.kaggle.com/datasets

## Community

- Contributing guide: [CONTRIBUTING.md](CONTRIBUTING.md)
- Code of conduct: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
