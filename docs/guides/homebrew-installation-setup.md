# Homebrew Installation Setup (macOS)

Use this guide if you are on macOS and want a single package manager workflow.

## 1) Install Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Verify:

```bash
brew --version
```

## 2) Install Core Tools with Brew

```bash
brew update
brew install python
brew install git
brew install --cask docker
```

Verify:

```bash
python3 --version
git --version
docker --version
```

## 3) Install Python Tooling

```bash
python3 -m pip install --upgrade pip
python3 -m pip install poetry black jupyter ipykernel pandas
```

Verify:

```bash
poetry --version
black --version
python3 -m jupyter --version
```

## 4) Optional: local learning workspace environment

```bash
python3 -m venv local/learning-workspace/.venv
source local/learning-workspace/.venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pandas jupyter ipykernel poetry black
```

## 5) Register reusable Jupyter kernel

```bash
python -m ipykernel install --user --name local-milestones --display-name "Local Milestones (.venv)"
```

## Notes

- On Windows/Linux, follow the OS-specific install methods in the milestone tickets.
- Docker Desktop may require opening the app once before CLI commands work fully.
