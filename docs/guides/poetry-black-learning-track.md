# Mandatory Learning Track: Poetry + Black

## Purpose

This track defines required Python project tooling for this repository.

Complete this during M0 Week 1 before starting notebook-heavy M1 work.

## Why Learn This

- `poetry` gives you dependency management + lockfile + environment workflow.
- `black` gives you consistent code formatting with one command.

## Prerequisites

- Python is installed and working.
- You can run basic terminal commands in this repository.

## Step 1: Install Poetry

Recommended official installer:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Then verify:

```bash
poetry --version
```

If the command is not found, fix Poetry installation and your shell `PATH` first:
- See [setup-verification.md](setup-verification.md) ("Poetry Not Found").

## Step 2: Create a Learning Branch

Do this in a branch so you can implement safely.

```bash
git checkout -b chore/poetry-black-learning
```

## Step 3: Initialize Poetry in This Repo

This repository already includes `pyproject.toml`.
Do not run `poetry init` here.

```bash
poetry config virtualenvs.in-project true
poetry install
```

If you want to confirm which packages are installed, inspect `pyproject.toml` and then run:

```bash
poetry show --tree
```

## Step 4: Run Commands Through Poetry

```bash
poetry run python --version
poetry run jupyter --version
poetry run black --version
```

## Step 5: Format Check Practice

Create a small test file and run formatter checks:

```bash
poetry run black .
poetry run black --check .
```

Expected behavior:
- first command formats files,
- second command returns success when formatting is clean.

## Step 6: Add Basic Black Configuration

`pyproject.toml` already includes basic Black configuration for this repo.

## Suggested Validation Commands

```bash
poetry check
poetry run python -c "import pandas as pd; print(pd.__version__)"
poetry run black --check .
```

## Required Notes

- This track is mandatory for all learners in this repository.
- Keep command usage consistent in notes/runbook (`poetry run ...`).
- If `poetry run ...` fails, fix that before moving to M1 tickets.

## Why `poetry.lock` Exists

This repo commits `poetry.lock` on purpose.
It pins exact dependency versions so two learners can run the same notebook/ETL steps and get the same environment.

`poetry.lock` should only change when:
- the project dependencies change intentionally (for example you add or upgrade a package), or
- you are asked to refresh the lockfile as part of a documented maintenance step.
