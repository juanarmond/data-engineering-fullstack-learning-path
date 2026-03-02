# Ticket: Install Python and Virtual Environment Tooling

## Milestone
Week 1 Onboarding

## Day
D03

## Goal
Install Python and run code inside an isolated virtual environment.

## Context
Python is the backbone for data engineering and backend work in this project.

## Tasks
- Install Python 3.11+.
- Create a virtual environment in `.venv`.
- Activate the environment and upgrade `pip`.

## How To Do It (Basic Steps)
- Install Python from `https://www.python.org/downloads/`.
- Confirm install with `python --version`.
- In your project folder run: `python -m venv .venv`.
- Activate it:
  - macOS/Linux: `source .venv/bin/activate`
  - Windows PowerShell: `.venv\\Scripts\\Activate.ps1`
- Upgrade pip: `python -m pip install --upgrade pip`.

## Acceptance Criteria
- Python and pip run correctly.
- Virtual environment can be created and activated.

## Verification
- `python --version`
- `python -m venv .venv`
- `source .venv/bin/activate` (macOS/Linux) or equivalent on Windows
- `python -m pip --version`

## Notes
Use `.venv` in project root and never commit it.
