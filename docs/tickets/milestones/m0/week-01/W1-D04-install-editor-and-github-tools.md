# Ticket: Install Editor and GitHub Workflow Tools

## Milestone
M0

## Day
D04

## Goal
Set up a code editor and connect local Git workflow to GitHub.

## Context
A usable editor and source-control workflow remove major beginner friction.

## Tasks
- Install VS Code (or another editor).
- Install recommended extensions for Python, markdown, and linting.
- Generate SSH key and add it to GitHub (or configure HTTPS auth).

## How To Do It (Basic Steps)
- Install VS Code from `https://code.visualstudio.com/`.
- Open Extensions and install `Python` and `Markdown All in One`.
- Generate SSH key:
  - `ssh-keygen -t ed25519 -C "you@example.com"`
- Copy public key and add it in GitHub: **Settings -> SSH and GPG keys**.
- Test connection: `ssh -T git@github.com`.

## Acceptance Criteria
- Editor opens project folders and integrated terminal works.
- Local machine can authenticate with GitHub.

## Verification
- `ssh -T git@github.com` (if using SSH)
- Open a local folder in editor and edit a markdown file.

## Notes
Document your editor setup in personal notes for future machines.
