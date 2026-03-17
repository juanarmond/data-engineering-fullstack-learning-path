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

From the repo root, install Poetry and then use it to create a project-local `.venv`:

```bash
python3 -m pip install --upgrade pip
curl -sSL https://install.python-poetry.org | python3 -
poetry config virtualenvs.in-project true
poetry install
```

Verify:

```bash
poetry --version
poetry run black --version
poetry run jupyter --version
```

## 4) Register reusable Jupyter kernel

```bash
poetry run python -m ipykernel install --user --name local-milestones --display-name "Local Milestones (.venv)"
```

If `poetry` is not on your global shell `PATH`, fix that before continuing:
- See [setup-verification.md](setup-verification.md) ("Poetry Not Found").

## Notes

- On Windows/Linux, follow the OS-specific install methods in the milestone tickets.
- Docker Desktop may require opening the app once before CLI commands work fully.
