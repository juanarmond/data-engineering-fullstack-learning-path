# Jupyter Notebook Run Commands

## Run Notebook in Place (CLI)

```bash
python -m jupyter nbconvert --to notebook --execute --inplace local/learning-workspace/m1/week-01/notebooks/m1_w1_lessons.ipynb
python -m jupyter nbconvert --to notebook --execute --inplace local/learning-workspace/m1/week-02/notebooks/m1_w2_analysis.ipynb
```

## Run With Shared Local Teacher Env

```bash
local/learning-workspace/.venv/bin/python -m jupyter nbconvert --to notebook --execute --inplace local/learning-workspace/m1/week-02/notebooks/m1_w2_analysis.ipynb
```

## VS Code Notebook Run Order

1. Select kernel `Local Milestones (.venv)`.
2. Restart kernel.
3. Run all cells top-to-bottom.

## Common Validation Commands

```bash
python -m jupyter --version
jupyter kernelspec list | rg local-milestones
```
