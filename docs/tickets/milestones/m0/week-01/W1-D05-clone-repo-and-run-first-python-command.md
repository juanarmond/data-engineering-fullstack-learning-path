# Ticket: Clone Repository and Run First Python Command

## Milestone
Week 1 Onboarding

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

## How To Do It (Basic Steps)
- Open the project on GitHub and click **Fork**.
- In your fork, copy the clone URL.
- Clone locally: `git clone <your-fork-url>`.
- Enter folder: `cd football-data-platform`.
- Run: `python -c "print('setup-ok')"`.

## Acceptance Criteria
- Repository exists locally and Git remote points to learner fork.
- Python command runs successfully in the project directory.

## Verification
- `git remote -v`
- `python --version`
- `python -c "print('setup-ok')"`

## Notes
If Python is missing, return to Day 3 and complete installation first.
