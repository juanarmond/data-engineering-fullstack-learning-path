# Ticket: Write curated output v1 (csv/parquet)

## Milestone
M2

## Day
D05

## Goal
Write curated output v1 (CSV/Parquet)

## Context
This ticket is part of Week 02 progression for M2 local ETL learning.

## Tasks
- Read the ticket fully before implementation.
- Document your steps and assumptions in clear language.
- Keep outputs reproducible by another learner.
- Create the load code in `local/learning-workspace/m2/week-02/src/m2_etl/load.py`.
- Write curated outputs to `local/learning-workspace/m2/week-02/data/curated/`.
- Write curated output file(s) to target folder.
- Keep output naming deterministic.
- Verify output can be reloaded successfully.
- Prefer `matches_curated.csv` as the required output; add Parquet only if the local environment already supports it.

## Starter Example To Copy

```python
from pathlib import Path
import pandas as pd


def write_curated(df: pd.DataFrame, output_path: Path) -> None:
    """Write the curated CSV to a deterministic location."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def main() -> None:
    input_path = Path("local/learning-workspace/m2/week-02/data/interim/matches_transformed.csv")
    output_path = Path("local/learning-workspace/m2/week-02/data/curated/matches_curated.csv")
    df = pd.read_csv(input_path)
    write_curated(df, output_path)
    print({"output_path": str(output_path), "rows": len(df)})


if __name__ == "__main__":
    main()
```

Copy this into your local workspace and then replace the TODO sections with your real logic.

## Acceptance Criteria
- Curated output exists at a predictable path in the Week 2 workspace.
- At least one successful reload check is documented.
- Commands or outputs can be reproduced with documented steps.

## Verification
- `poetry run python local/learning-workspace/m2/week-02/src/m2_etl/load.py`
- `ls -la local/learning-workspace/m2/week-02/data/curated`

## Notes
Keep scope limited to this ticket and avoid jumping ahead.
## Supplemental Reading

- Docker Documentation: https://docs.docker.com/
- pandas Documentation: https://pandas.pydata.org/docs/
- Data validation (concept): https://en.wikipedia.org/wiki/Data_validation
