# Ticket: Raw Data Download and Storage Conventions

## Milestone
M1

## Day
D02

## Goal
Download first raw data files and store them with clear naming conventions.

## Context
Consistent raw data organization prevents confusion and makes automation easier later.

## Tasks
- Create or confirm raw data folder structure (for example `data/raw/<source>/`).
- Download selected CSV file(s) manually.
- Define and apply file naming convention (league, season, date if needed).
- Document where files are stored and why the convention was chosen.

## Acceptance Criteria
- Raw files exist in a predictable folder.
- File names follow one defined convention.
- Storage convention is documented in notes.

## Verification
- Manual check of folder structure and filenames.
- Confirm at least one dataset opens successfully.

## OS and Research Note
Command usage can vary by OS and shell. If a command in this ticket does not work on your machine, research the equivalent command for your OS and record what you used in your notes.

## Notes
Do not automate download in this ticket.
## Supplemental Reading

- pandas Documentation: https://pandas.pydata.org/docs/
- Jupyter Documentation: https://docs.jupyter.org/
- Python pathlib: https://docs.python.org/3/library/pathlib.html

