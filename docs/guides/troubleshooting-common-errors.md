# Troubleshooting Common Errors

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
source local/learning-workspace/.venv/bin/activate
python -m pip install pandas jupyter ipykernel
```

## Kernel Not Visible in VS Code

```bash
python -m ipykernel install --user --name local-milestones --display-name "Local Milestones (.venv)"
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
