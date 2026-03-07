# Mandatory Learning Track: Poetry + Black

## Purpose

This track defines required Python project tooling for this repository.

Complete this after M0 Week 1 and before finishing M1 Week 2.

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

If the command is not found, add Poetry's bin directory to your shell path based on your OS.

## Step 2: Create a Learning Branch

Do this in a branch so you can implement safely.

```bash
git checkout -b chore/poetry-black-learning
```

## Step 3: Initialize Poetry in This Repo

```bash
poetry init
```

Use defaults if you are unsure, then add core packages:

```bash
poetry add pandas jupyter
poetry add --group dev black
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

Add this in `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ["py311", "py312"]
```

## Suggested Validation Commands

```bash
poetry check
poetry run python -c "import pandas as pd; print(pd.__version__)"
poetry run black --check .
```

## Required Notes

- This track is mandatory for all learners in this repository.
- Keep command usage consistent in notes/runbook (`poetry run ...`).
