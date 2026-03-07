# Python Env and Kernel Setup

## Shared Local Teacher Environment

```bash
python -m venv local/learning-workspace/.venv
source local/learning-workspace/.venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pandas jupyter ipykernel poetry black
python -m ipykernel install --user --name local-milestones --display-name "Local Milestones (.venv)"
```

## Verify

```bash
local/learning-workspace/.venv/bin/python --version
local/learning-workspace/.venv/bin/poetry --version
local/learning-workspace/.venv/bin/black --version
jupyter kernelspec list | rg local-milestones
```

## Use in VS Code

1. Open notebook.
2. Click `Select Kernel`.
3. Choose `Local Milestones (.venv)`.
