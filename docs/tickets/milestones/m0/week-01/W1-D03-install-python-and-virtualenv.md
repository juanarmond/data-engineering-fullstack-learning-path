# Ticket: Install Python and Virtual Environment Tooling

## Milestone
M0

## Day
D03

## Goal
Install Python and run code inside an isolated environment with Poetry-based dependency management.

## Context
Python is the backbone for data engineering and backend work in this project.

## Tasks
- Install Python 3.11+.
- Create a virtual environment in `.venv`.
- Activate the environment and upgrade `pip`.
- Install Poetry.
- Install Black using Poetry dev dependencies.

## How To Do It (Basic Steps)
- On macOS, prefer Homebrew setup from [docs/guides/homebrew-installation-setup.md](../../../guides/homebrew-installation-setup.md).
- Alternative: install Python from `https://www.python.org/downloads/`.
- Confirm install with `python --version` (or `python3 --version` when applicable).
- In your project folder run: `python -m venv .venv`.
- Activate it:
  - macOS/Linux: `source .venv/bin/activate`
  - Windows PowerShell: `.venv\\Scripts\\Activate.ps1`
- Upgrade pip: `python -m pip install --upgrade pip`.
- Install Poetry (official installer): `curl -sSL https://install.python-poetry.org | python3 -`.
- Verify Poetry: `poetry --version`.
- Initialize project metadata if missing: `poetry init -n`.
- Add Black as a dev dependency: `poetry add --group dev black`.
- Verify formatter: `poetry run black --version`.

## Acceptance Criteria
- Python and pip run correctly.
- Virtual environment can be created and activated.
- Poetry is installed and available in terminal.
- Black is installed and runnable through Poetry.

## Verification
- `python --version`
- `python -m venv .venv`
- `source .venv/bin/activate` (macOS/Linux) or equivalent on Windows
- `python -m pip --version`
- `poetry --version`
- `poetry run black --version`

## Notes
Use `.venv` in project root and never commit it.

Mandatory follow-up:
- Complete [docs/guides/poetry-black-learning-track.md](../../../guides/poetry-black-learning-track.md).
## Supplemental Reading

- Git Documentation: https://git-scm.com/doc
- Python Tutorial: https://docs.python.org/3/tutorial/
- VS Code Docs: https://code.visualstudio.com/docs
