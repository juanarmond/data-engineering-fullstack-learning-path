# Ticket: Create First Branch, Commit, and Pull Request

## Milestone
Week 1 Onboarding

## Day
D07

## Goal
Practice the complete collaboration cycle with one small documentation change.

## Context
Branching, committing, and opening pull requests are daily workflow basics.

## Tasks
- Create a branch from main.
- Make a tiny docs improvement.
- Commit with a clear message and push branch.
- Open a pull request to your fork or upstream project.

## How To Do It (Basic Steps)
- Start from main: `git checkout main`.
- Create a branch: `git checkout -b docs/week1-practice`.
- Edit one markdown file (for example fix one typo).
- Stage and commit:
  - `git add <file>`
  - `git commit -m "docs: week 1 practice update"`
- Push branch: `git push -u origin docs/week1-practice`.
- Open GitHub and create a pull request from this branch.

## Acceptance Criteria
- Branch and commit history are clean and readable.
- Pull request includes description and verification notes.

## Verification
- `git checkout -b docs/week1-practice`
- `git status`
- `git log --oneline -n 3`
- Confirm PR page opens with your branch diff.

## Notes
Use conventional commit style for the commit message.
