# Tickets Guide

Use tickets as the day-by-day execution plan.

## How To Navigate

Follow this hierarchy:
1. [../../README.md](../../README.md) (project-level)
2. [../roadmap.md](../roadmap.md) (phase-level)
3. `milestones/<milestone>/README.md` (milestone-level)
4. `milestones/<milestone>/week-<nn>/README.md` (week-level)
5. day tickets (execution-level)

## Milestone Entry Points

- [docs/tickets/milestones/m0/README.md](milestones/m0/README.md)
- [docs/tickets/milestones/m1/README.md](milestones/m1/README.md)
- [docs/tickets/milestones/m2/README.md](milestones/m2/README.md)

## Recommended Execution Path

1. `milestones/m0/week-01/`
2. `milestones/m1/week-01/`
3. `milestones/m1/week-02/`
4. `milestones/m1/week-03/`
5. `milestones/m1/week-04/`
6. `milestones/m2/week-01/`
7. `milestones/m2/week-02/`
8. `milestones/m2/week-03/`
9. `milestones/m2/week-04/`

## Ticket Rules

A good ticket must include:
- goal,
- context,
- tasks,
- acceptance criteria,
- verification steps.

## Getting Stuck Is Normal

This repo is designed for learning, so it is normal to get stuck sometimes.
That does not mean you are failing.

When you are stuck:
- re-read the current ticket and week README,
- compare the expected output path with what you actually created,
- read the full error message,
- try the troubleshooting/setup guides,
- check official docs for the tool or library involved,
- write down what you tried in your notes before moving on.

Good learning progress includes debugging, research, retrying, and fixing mistakes.
The goal is not to avoid all problems.
The goal is to learn how to recover when problems happen.

## Setup Verification (When Things Feel Broken)

If a verification step fails and you are not sure what to do next, use:
- [docs/guides/setup-verification.md](../guides/setup-verification.md)

## Workspace Folder Rule (Mandatory)

Before starting any milestone/week tickets, create the local workspace path:
- `local/learning-workspace/<milestone>/week-<nn>/`

Example:
- `local/learning-workspace/m1/week-01/`
- `local/learning-workspace/m1/week-02/`
- `local/learning-workspace/m1/week-03/`
- `local/learning-workspace/m1/week-04/`
- `local/learning-workspace/m2/week-01/`

Store learner-created notebooks, notes, raw files, scripts, and weekly handoff files inside `local/learning-workspace/` unless a ticket explicitly says otherwise.
This folder is gitignored on purpose.

Recommended milestone subfolders:
- `notebooks/` for notebook work
- `notes/` for markdown handoff notes and summaries
- `data/raw/`, `data/interim/`, `data/curated/` for milestone data outputs when needed
- `src/` and `tests/` for later ETL milestones

## Weekly Cadence

At week end:
- mark completed tickets,
- list blockers,
- confirm deliverables,
- write handoff notes,
- then move forward.

## Success Check

A learner is ready to move forward when they can answer all of these questions:
- What is this week trying to teach me?
- What file or output am I supposed to create?
- Where should that output live?
- How do I verify that my work succeeded?
