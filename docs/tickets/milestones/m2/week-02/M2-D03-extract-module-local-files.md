# Ticket: Build extract step for local source files

## Milestone
M2

## Day
D03

## Goal
Build extract step for local source files

## Context
This ticket is part of Week 02 progression for M2 local ETL learning.

## Tasks
- Read the ticket fully before implementation.
- Document your steps and assumptions in clear language.
- Keep outputs reproducible by another learner.
- Create the extract code in `local/learning-workspace/m2/week-02/src/m2_etl/extract.py`.
- Read from the dataset path documented in `local/learning-workspace/m1/week-04/notes/d07-m2-prep.md`, or from the copied Week 2 raw file if you chose to duplicate it in D02.
- Implement extract step that reads source file(s).
- Validate source readability and basic schema availability.
- Output extract summary metrics (rows/columns).

## Starter Example To Copy

```python
from pathlib import Path
import pandas as pd


def extract_source(source_csv: Path) -> pd.DataFrame:
    """Read the source CSV and return a DataFrame."""
    # TODO: add your own existence checks and schema checks here.
    return pd.read_csv(source_csv)


def main() -> None:
    # Replace this example path with the dataset path recorded in:
    # local/learning-workspace/m1/week-04/notes/d07-m2-prep.md
    source_csv = Path("local/learning-workspace/m1/data/raw/your_chosen_dataset.csv")
    df = extract_source(source_csv)
    print({"rows": len(df), "columns": list(df.columns)})


if __name__ == "__main__":
    main()
```

Copy this into your local workspace and then replace the TODO sections with your real logic.

## Acceptance Criteria
- Extract module can be run from the repo root with a documented command.
- Extract output confirms the expected football match columns are available before transform work begins.
- Commands or outputs can be reproduced with documented steps.

## Verification
- `poetry run python local/learning-workspace/m2/week-02/src/m2_etl/extract.py`
- Re-run the same command after changing nothing and confirm the same source is loaded successfully.

## Notes
Keep scope limited to this ticket and avoid jumping ahead.
## Supplemental Reading

- Docker Documentation: https://docs.docker.com/
- pandas Documentation: https://pandas.pydata.org/docs/
- Data validation (concept): https://en.wikipedia.org/wiki/Data_validation
