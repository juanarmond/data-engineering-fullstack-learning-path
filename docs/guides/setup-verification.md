# Setup Verification (OS-Aware)

Use this guide when:
- you just finished setup and want to confirm everything is working, or
- a ticket says "verify" and you are not sure what to run, or
- you are about to start M1/M2 and want to avoid environment surprises.

This repo uses one canonical command style:
- `poetry ...`
- `poetry run ...`

If `poetry` is not found, follow the "Poetry Not Found" section below.

## Quick Verify (All OS)

From the repo root:

```bash
poetry --version
poetry install
poetry run python --version
poetry run black --version
poetry run python -m jupyter --version
```

## Verify Jupyter Kernel Exists

We use a shared kernel name so notebooks run in the same environment:
- Kernel name: `local-milestones`
- Display name: `Local Milestones (.venv)`

List kernels:

```bash
poetry run python -m jupyter kernelspec list
```

Then confirm `local-milestones` appears.

Filter the output (optional):

macOS/Linux:

```bash
poetry run python -m jupyter kernelspec list | rg local-milestones
```

Windows PowerShell:

```powershell
poetry run python -m jupyter kernelspec list | Select-String local-milestones
```

If the kernel is missing, register it:

```bash
poetry run python -m ipykernel install --user --name local-milestones --display-name "Local Milestones (.venv)"
```

## Verify Required Workspace Folders Exist

This repo keeps learner outputs under `local/learning-workspace/` (gitignored on purpose).

macOS/Linux:

```bash
mkdir -p local/learning-workspace/m0/week-01
ls -la local/learning-workspace
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force -Path local\\learning-workspace\\m0\\week-01 | Out-Null
Get-ChildItem local\\learning-workspace
```

## Beginner Sanity Check Harness (Recommended)

Run the tracked sanity check (it prints clear pass/fail messages):

```bash
poetry run python scripts/sanity_check.py
```

If you want it to create missing workspace folders and register the kernel automatically:

```bash
poetry run python scripts/sanity_check.py --fix
```

## Poetry Not Found

If `poetry --version` fails with "command not found":

1. Re-check that Poetry is installed using the setup steps for your OS (M0 Week 1 Day 3 and the setup guides).
2. Ensure Poetry's install directory is on your shell `PATH`.

Tip: the Poetry installer prints the install location and the PATH line you should add.
Copy that into your shell profile and open a new terminal.
