#!/usr/bin/env python3
"""
Beginner sanity check for this learning-path repository.

Run from the repo root (recommended):
  poetry run python scripts/sanity_check.py

This script checks:
- Python version
- required packages import
- Jupyter kernel registration (local-milestones)
- required workspace folders under local/learning-workspace/

Use --fix to create missing workspace folders and register the kernel.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


KERNEL_NAME = "local-milestones"
KERNEL_DISPLAY_NAME = "Local Milestones (.venv)"


def _run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, capture_output=True)


def _print_result(ok: bool, label: str, detail: str | None = None) -> None:
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}")
    if detail:
        # Keep details readable for beginners.
        for line in detail.strip().splitlines():
            print(f"  {line}")


def check_python_version() -> bool:
    major, minor = sys.version_info[:2]
    ok = (major, minor) >= (3, 11)
    _print_result(
        ok,
        "Python version >= 3.11",
        f"Detected: {sys.version.splitlines()[0]}",
    )
    return ok


def check_imports() -> bool:
    ok = True
    for mod in ["pandas", "jupyter", "ipykernel", "black"]:
        try:
            __import__(mod)
            _print_result(True, f"Import '{mod}'")
        except Exception as e:  # noqa: BLE001 - we want beginner-friendly output
            ok = False
            _print_result(False, f"Import '{mod}'", repr(e))
    return ok


def kernelspecs() -> dict:
    # Use jupyter CLI to match what students see in tickets.
    cp = _run([sys.executable, "-m", "jupyter", "kernelspec", "list", "--json"])
    if cp.returncode != 0:
        raise RuntimeError(cp.stderr.strip() or cp.stdout.strip() or "kernelspec list failed")
    return json.loads(cp.stdout)


def check_kernel_present() -> bool:
    try:
        data = kernelspecs()
    except Exception as e:  # noqa: BLE001
        _print_result(False, "Jupyter kernelspec list", repr(e))
        return False

    specs = data.get("kernelspecs", {}) if isinstance(data, dict) else {}
    ok = KERNEL_NAME in specs
    if ok:
        _print_result(True, f"Kernel '{KERNEL_NAME}' is registered")
    else:
        known = ", ".join(sorted(specs.keys())) if specs else "(none)"
        _print_result(False, f"Kernel '{KERNEL_NAME}' is registered", f"Found kernels: {known}")
    return ok


def fix_kernel() -> bool:
    cp = _run(
        [
            sys.executable,
            "-m",
            "ipykernel",
            "install",
            "--user",
            "--name",
            KERNEL_NAME,
            "--display-name",
            KERNEL_DISPLAY_NAME,
        ]
    )
    ok = cp.returncode == 0
    _print_result(ok, f"Register kernel '{KERNEL_NAME}'", cp.stderr.strip() or cp.stdout.strip() or None)
    return ok


def check_workspace_folders(fix: bool) -> bool:
    repo_root = Path(__file__).resolve().parents[1]
    workspace_root = repo_root / "local" / "learning-workspace"

    required = [
        workspace_root,
        workspace_root / "m0" / "week-01",
    ]

    ok = True
    for p in required:
        if p.exists():
            _print_result(True, f"Workspace path exists: {p.relative_to(repo_root)}")
            continue

        if fix:
            try:
                p.mkdir(parents=True, exist_ok=True)
                _print_result(True, f"Created workspace path: {p.relative_to(repo_root)}")
                continue
            except Exception as e:  # noqa: BLE001
                ok = False
                _print_result(False, f"Create workspace path: {p.relative_to(repo_root)}", repr(e))
                continue

        ok = False
        _print_result(False, f"Workspace path exists: {p.relative_to(repo_root)}", "Run mkdir (see docs/guides/setup-verification.md).")

    return ok


def main() -> int:
    parser = argparse.ArgumentParser(description="Beginner sanity check for the learning-path repo.")
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Create missing workspace folders and register the notebook kernel if needed.",
    )
    args = parser.parse_args()

    ok = True
    ok &= check_python_version()
    ok &= check_imports()

    kernel_ok = check_kernel_present()
    if not kernel_ok and args.fix:
        kernel_ok = fix_kernel() and check_kernel_present()
    ok &= kernel_ok

    ok &= check_workspace_folders(fix=args.fix)

    if ok:
        print("\nAll sanity checks passed.")
        return 0

    print("\nOne or more sanity checks failed.")
    print("Next: follow docs/guides/setup-verification.md or re-run with --fix if appropriate.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

