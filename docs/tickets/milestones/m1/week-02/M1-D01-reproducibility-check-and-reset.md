# Ticket: Reproducibility Check and Reset

## Milestone
M1

## Day
D01

## Goal
Confirm that Week 1 outputs can be reproduced from a clean start.

## Context
Engineering work must be reproducible by another contributor on another machine.

## Tasks
- Re-open the Week 1 notebook from a fresh kernel.
- Re-run all cells top to bottom.
- Record any manual steps that were required but not documented.
- Fix notebook order issues (hidden state, missing imports, out-of-order cells).

## Acceptance Criteria
- Notebook runs end-to-end from a clean kernel.
- Hidden/manual steps are documented.
- Reproducibility issues are listed with fixes.

## Verification
- Restart kernel and run all cells.
- Manual review of reproducibility notes.

## OS and Research Note
Kernel restart flow, terminal commands, and environment handling vary by OS and tool setup. If any command fails, research the OS-specific equivalent and document it in your notes.

## Notes
Do not add new analysis scope in this ticket.
