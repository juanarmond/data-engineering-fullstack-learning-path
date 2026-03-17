# Ticket: Basic Git and Python Checks

## Milestone
M0

## Day
D06

## Goal
Practice basic project checks using Git and Python commands.

## Context
Consistent command-line checks are a core daily engineering habit.

## Tasks
- Confirm repository status and current branch.
- Confirm Python version in the project environment.
- Run one simple Python script command.
- Confirm Poetry and Black are available and working.
- Confirm `local/learning-workspace/` exists.
- Confirm notebook kernel readiness for next milestone.

## How To Do It (Basic Steps)
- Open terminal in the project folder.
- Run `git status` to see current file state.
- Run `git branch --show-current` to confirm current branch.
- Run `python --version`.
- Run `python -c "print('week-1-checks-ok')"`.
- Run `poetry --version`.
- Run `poetry run python --version`.
- Run `poetry run black --check .`.
- Run `ls -la local`.
- Run `jupyter kernelspec list`.
- If one command fails, fix it before moving on.
If you are unsure what to fix, follow [docs/guides/setup-verification.md](../../../guides/setup-verification.md).

Optional (recommended):
- Run the beginner sanity check harness: `poetry run python scripts/sanity_check.py`

## Acceptance Criteria
- Learner can explain what each command confirms.
- All verification commands complete successfully.
- Poetry and Black checks pass without errors.
- Local learning workspace path exists and is visible.
- At least one usable local notebook kernel is available.

## Verification
- `git status`
- `git branch --show-current`
- `python --version`
- `python -c "print('week-1-checks-ok')"`
- `poetry --version`
- `poetry run python --version`
- `poetry run black --check .`
- `ls -la local`
- `jupyter kernelspec list`

## Notes
If commands fail, document the issue and fix in setup notes.

Poetry + Black are part of the mandatory tooling baseline for this project.
## Supplemental Reading

- Git Documentation: https://git-scm.com/doc
- Python Tutorial: https://docs.python.org/3/tutorial/
- VS Code Docs: https://code.visualstudio.com/docs
