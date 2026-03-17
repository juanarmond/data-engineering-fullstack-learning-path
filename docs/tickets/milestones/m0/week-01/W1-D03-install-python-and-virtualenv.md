# Ticket: Install Python and Poetry Environment Tooling

## Milestone
M0

## Day
D03

## Goal
Install Python and set up the Poetry-managed project environment used by this repository.

## Context
Python is the backbone for data engineering and backend work in this project.

## Tasks
- Install Python 3.11+.
- Install Poetry.
- Configure Poetry to create the environment in `.venv`.
- Install the tracked project dependencies from `pyproject.toml`.
- Verify Black through Poetry.

## How To Do It (Basic Steps)
- On macOS, prefer Homebrew setup from [docs/guides/homebrew-installation-setup.md](../../../guides/homebrew-installation-setup.md).
- Alternative: install Python from `https://www.python.org/downloads/`.
- Confirm install with `python --version` (or `python3 --version` when applicable).
- Install Poetry (official installer): `curl -sSL https://install.python-poetry.org | python3 -`.
- Verify Poetry: `poetry --version`.
- In this repo, run `poetry config virtualenvs.in-project true`.
- Install the tracked dependencies: `poetry install`.
- Verify formatter: `poetry run black --version`.
- Verify Python through Poetry: `poetry run python --version`.
If something fails, use [docs/guides/setup-verification.md](../../../guides/setup-verification.md) to verify the full setup path.

## Acceptance Criteria
- Python and pip run correctly.
- Poetry is installed and available in terminal.
- The repo creates a Poetry-managed `.venv`.
- Black is installed and runnable through Poetry.

## Verification
- `python --version`
- `poetry --version`
- `poetry install`
- `ls -la .venv`
- `poetry run black --version`
- `poetry run python --version`

## Notes
Use `.venv` in project root and never commit it.

Important mental model:
- You are not manually building a separate `venv` with `pip install ...`.
- Poetry is the tool that creates and manages the project environment for this repo.
- The `.venv/` folder is just the local environment Poetry creates after `poetry install`.

Mandatory follow-up:
- Complete [docs/guides/poetry-black-learning-track.md](../../../guides/poetry-black-learning-track.md).
## Supplemental Reading

- Git Documentation: https://git-scm.com/doc
- Python Tutorial: https://docs.python.org/3/tutorial/
- VS Code Docs: https://code.visualstudio.com/docs
