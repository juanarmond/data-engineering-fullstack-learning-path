# Jupyter Notebook Run Commands

## Run Notebook in Place (CLI)

```bash
python -m jupyter nbconvert --to notebook --execute --inplace local/learning-workspace/m1/week-01/notebooks/m1_w1_python_basics.ipynb
python -m jupyter nbconvert --to notebook --execute --inplace local/learning-workspace/m1/week-02/notebooks/m1_w2_sql_basics.ipynb
python -m jupyter nbconvert --to notebook --execute --inplace local/learning-workspace/m1/week-03/notebooks/m1_w3_analysis.ipynb
python -m jupyter nbconvert --to notebook --execute --inplace local/learning-workspace/m1/week-04/notebooks/m1_w4_analysis.ipynb
```

## Run With Shared Local Teacher Env

```bash
poetry run python -m jupyter nbconvert --to notebook --execute --inplace local/learning-workspace/m1/week-01/notebooks/m1_w1_python_basics.ipynb
poetry run python -m jupyter nbconvert --to notebook --execute --inplace local/learning-workspace/m1/week-02/notebooks/m1_w2_sql_basics.ipynb
poetry run python -m jupyter nbconvert --to notebook --execute --inplace local/learning-workspace/m1/week-04/notebooks/m1_w4_analysis.ipynb
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
