# Troubleshooting Common Errors

## Before You Panic

Getting stuck is normal in this repo.
Many tickets are meant to teach you how to read errors, verify assumptions, and recover step by step.

Use this recovery order:
1. Re-read the current ticket and week README.
2. Check the exact file path the ticket expects.
3. Read the full error message, not just the first line.
4. Restart the notebook kernel or rerun the command from a clean state.
5. Use the setup verification guide if tooling feels broken.
6. Look up the official docs for the command, library, or error you hit.
7. Write down what you tried and what changed.

If you solve the issue after research and retrying, that still counts as successful progress.

## `FileNotFoundError` for CSV

Checks:

```bash
pwd
ls -la local/learning-workspace/m1/data/raw/
```

Fix:
- Confirm notebook path assumptions and `CONFIG['data_path']`.

## `No module named pandas` (or other package)

```bash
poetry install
poetry run python -c "import pandas as pd; print(pd.__version__)"
```

## Kernel Not Visible in VS Code

```bash
poetry run python -m ipykernel install --user --name local-milestones --display-name "Local Milestones (.venv)"
jupyter kernelspec list | rg local-milestones
```

Then reload VS Code window and reselect kernel.

## Notebook Executes in CLI but Fails in UI

Fix sequence:
1. Select correct kernel.
2. Restart kernel.
3. Run all cells in order.
4. Check that section config cells were executed first.

## `nbconvert` Permission/Port Errors in Restricted Shell

- Use VS Code UI execution if shell restrictions block kernel ports.
- Or run command from a terminal/session with required permissions.
