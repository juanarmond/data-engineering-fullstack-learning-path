# Terminal Quick Reference

## Navigation

```bash
pwd
ls -la
cd docs
cd ..
```

## Search

```bash
rg "M1-D06" docs/
rg --files docs/tickets/milestones/m1/week-02
```

## File and Folder Operations

```bash
mkdir -p local/learning-workspace/m1/week-01/notebooks
cp source.csv local/learning-workspace/m1/data/raw/BRA.csv
mv old-name.md new-name.md
rm -rf local/learning-workspace/m1/week-02/data
```

## Python and Pip

```bash
python --version
python -m pip --version
python -m pip install pandas jupyter
```

## Useful Checks

```bash
git status --short
find local/learning-workspace -maxdepth 4 -type f | sort
```
