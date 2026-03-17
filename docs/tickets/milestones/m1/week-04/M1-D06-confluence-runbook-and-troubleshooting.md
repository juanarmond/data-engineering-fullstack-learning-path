# Ticket: Confluence-Style Runbook and Troubleshooting

## Milestone
M1

## Day
D06

## Goal
Document repeatable run steps and troubleshooting guidance in a Confluence-style runbook format inside the notebook.

## Context
A notebook-embedded runbook helps new contributors execute work without switching between many files.
This ticket also introduces Confluence-style documentation habits used in teams for operational handoff.

Confluence references:
- What is Confluence: https://www.atlassian.com/software/confluence
- Confluence documentation basics: https://support.atlassian.com/confluence-cloud/docs/get-started-with-confluence/

## Tasks
- Add a notebook section with prerequisites and run order.
- Add copy-paste-ready commands used for this week.
- Add common failure cases and quick fixes.
- Link key notebook sections for loading, profiling, checks, and report summary.
- Keep runbook content under a dedicated markdown heading separate from analysis sections.
- Structure the runbook section in Confluence-style blocks:
  - `Purpose`
  - `Prerequisites`
  - `Run Steps`
  - `Troubleshooting`
  - `Open Issues / Next Actions`
- Delivery format can be either:
  - New markdown cell section inside the Week 4 notebook, or
  - Separate markdown file (recommended: `local/learning-workspace/m1/week-04/notes/d06-runbook.md`) linked from the notebook.
- Include this required report content:
  - Notebook name and dataset path used
  - Environment/kernel used
  - Exact run command(s)
  - Expected success outputs/checkpoints
  - Common failure scenarios and fixes
  - Open issues and recommended next actions

## Acceptance Criteria
- A new learner can run the notebook workflow using notebook guidance.
- Common blockers and fixes are clearly listed.
- Commands and referenced paths are valid.
- Runbook section is clearly organized in Confluence-style headings.
- Report includes all required content items listed in this ticket.
- If using a separate markdown file, notebook contains a clear link/reference to it.

## Verification
- Follow notebook run steps from top to bottom.
- Confirm troubleshooting notes are practical and specific.
- Confirm all required report content is present.
- If separate file is used, confirm the notebook link/reference resolves correctly.

## OS and Research Note
Command usage differs by OS. When commands vary, research and use the correct command for your OS, then document the equivalent in the notebook.

## Notes
Prioritize clarity and copy-paste-ready guidance.
Do not add new analysis in this ticket; focus on execution documentation quality.
## Supplemental Reading

- pandas Documentation: https://pandas.pydata.org/docs/
- Jupyter Documentation: https://docs.jupyter.org/
- Python pathlib: https://docs.python.org/3/library/pathlib.html
