# Python Env and Kernel Setup

## Canonical Repo Environment

```bash
poetry config virtualenvs.in-project true
poetry install
poetry run python -m ipykernel install --user --name local-milestones --display-name "Local Milestones (.venv)"
```

## Verify

```bash
poetry run python --version
poetry --version
poetry run black --version
poetry run python -m jupyter kernelspec list
```

## Use in VS Code

1. Open notebook.
2. Click `Select Kernel`.
3. Choose `Local Milestones (.venv)`.
