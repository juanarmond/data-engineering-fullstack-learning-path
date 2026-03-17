# Week 01 Summary (M2 Setup Foundations)

## Entry Criteria (Before Starting)

- M1 Week 1 to Week 4 deliverables completed.
- `local/learning-workspace/` available in repo root.
- Python + Poetry + Black baseline already installed from M0/M1.
- Week folder created: `local/learning-workspace/m2/week-01/`.
- M1 handoff artifacts are still present:
  - the learner's chosen raw dataset path, documented in `local/learning-workspace/m1/week-04/notes/d07-m2-prep.md`
  - `local/learning-workspace/m1/week-03/notes/d05-quality-checks.md`
  - `local/learning-workspace/m1/week-04/notes/d07-m2-prep.md`

Run these checks before Day 1:
- `ls -la local/learning-workspace/m2/week-01`
- `ls -la local/learning-workspace/m1/data/raw`
- `poetry run python --version`
- `poetry run black --version`
- `jupyter kernelspec list`
If any check fails, use: [docs/guides/setup-verification.md](../../../../guides/setup-verification.md)

## OS Command Note (Important)

Install and verification commands can differ by OS. If a command fails, use the OS-equivalent command and document what you used.

## Why Docker In This Week

M2 still runs the ETL work locally with Poetry and local files.
Docker is introduced here so beginners start learning:
- the difference between local code and a packaged environment,
- basic container vocabulary used in later milestones,
- how teams make tools and services more reproducible across machines.

You are not using Docker because the Week 2 ETL requires it today.
You are using it here because it prepares you for later platform and service work.

## What You Will Learn This Week

- Install and verify Docker Desktop.
- Understand Docker image vs container basics.
- Confirm local workspace conventions for M2 work.
- Run a first local container command safely.
- Document setup in beginner-friendly run notes.

## Weekly Deliverables

- Docker installed and verified (`docker --version`, `docker run hello-world`).
- Basic image/container practice notes.
- Local workspace readiness checks documented.
- Setup runbook in Confluence-style format.
- Weekly setup signoff and open issues list.

## Review Checkpoints

- Checkpoint A (after D02): Docker concepts are understandable in plain language.
- Checkpoint B (after D04): first container command runs and logs are readable.
- Checkpoint C (after D07): setup blockers and next actions are documented for Week 2.

## Skills Focus

- Docker fundamentals
- Environment verification
- Runbook discipline
- Beginner ops habits

## Learning Resources

Official docs:
- Docker Docs: https://docs.docker.com/
- Docker Get Started: https://docs.docker.com/get-started/
- Atlassian Confluence: https://www.atlassian.com/software/confluence
- Homebrew docs: https://brew.sh/

Project guide:
- [docs/guides/homebrew-installation-setup.md](../../../../guides/homebrew-installation-setup.md)

## Tickets in This Week

- [M2-D01-install-docker-desktop.md](M2-D01-install-docker-desktop.md)
- [M2-D02-images-vs-containers-basics.md](M2-D02-images-vs-containers-basics.md)
- [M2-D03-preflight-readiness-check.md](M2-D03-preflight-readiness-check.md)
- [M2-D04-first-docker-run-and-logs.md](M2-D04-first-docker-run-and-logs.md)
- [M2-D05-docker-compose-basics-optional.md](M2-D05-docker-compose-basics-optional.md)
- [M2-D06-setup-runbook-confluence-style.md](M2-D06-setup-runbook-confluence-style.md)
- [M2-D07-weekly-review-and-setup-signoff.md](M2-D07-weekly-review-and-setup-signoff.md)

## Exit Criteria (Definition of Done)

Week 1 is complete when:
- local setup is stable for ETL work,
- the student has confirmed the M1 dataset and notes they will carry into M2,
- Docker basics are verified,
- runbook steps are clear to another learner,
- setup blockers are documented with fixes or next actions.
