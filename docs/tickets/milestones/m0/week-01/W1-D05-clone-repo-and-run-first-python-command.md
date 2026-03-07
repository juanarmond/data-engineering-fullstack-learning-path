# Ticket: Clone Repository and Run First Python Command

## Milestone
M0

## Day
D05

## Goal
Clone the project and confirm Python runs correctly in the project folder.

## Context
Before advanced checks, beginners should confirm local repo setup and Python execution.

## Tasks
- Fork repository on GitHub.
- Clone the fork locally.
- Run a simple Python command in project root.
- Create local learning workspace folder structure:
  - `local/learning-workspace/`
  - `local/learning-workspace/m0/week-01/`

## How To Do It (Basic Steps)
- Open the project on GitHub and click **Fork**.
- In your fork, copy the clone URL.
- Clone locally: `git clone <your-fork-url>`.
- Enter folder: `cd <your-repo-folder>`.
- Create learning workspace: `mkdir -p local/learning-workspace/m0/week-01`.
- Run: `python -c "print('setup-ok')"`.

## Acceptance Criteria
- Repository exists locally and Git remote points to learner fork.
- Python command runs successfully in the project directory.
- `local/learning-workspace/m0/week-01/` exists in the repo root.

## Verification
- `git remote -v`
- `python --version`
- `python -c "print('setup-ok')"`
- `ls -la local`
- `ls -la local/learning-workspace/m0/week-01`

## Notes
If Python is missing, return to Day 3 and complete installation first.
## Supplemental Reading

- Git Documentation: https://git-scm.com/doc
- Python Tutorial: https://docs.python.org/3/tutorial/
- VS Code Docs: https://code.visualstudio.com/docs
