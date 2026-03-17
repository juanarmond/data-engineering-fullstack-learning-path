# Ticket: Apply first transform rules from m1 quality findings

## Milestone
M2

## Day
D04

## Goal
Apply first transform rules from M1 quality findings

## Context
This ticket is part of Week 02 progression for M2 local ETL learning.

## Tasks
- Read the ticket fully before implementation.
- Document your steps and assumptions in clear language.
- Keep outputs reproducible by another learner.
- Create the transform code in `local/learning-workspace/m2/week-02/src/m2_etl/transform.py`.
- Translate the concrete M1 findings into rules:
  - keep nullable outcome handling explicit for the flagged Chapecoense match row,
  - decide how to handle sparse odds columns,
  - preserve a stable match-level key using `Season`, `Date`, `Home`, `Away`.
- Apply transform rules derived from M1 quality findings.
- Standardize key columns/types.
- Document any row-level exceptions.

## Starter Example To Copy

```python
import pandas as pd


def transform_matches(df: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned DataFrame for curated output."""
    cleaned = df.copy()
    # TODO: rename columns, handle nulls, and build a stable match key.
    return cleaned


def main() -> None:
    input_path = "local/learning-workspace/m2/week-02/data/interim/matches_extracted.csv"
    df = pd.read_csv(input_path)
    cleaned = transform_matches(df)
    print(cleaned.head())


if __name__ == "__main__":
    main()
```

Copy this into your local workspace and then replace the TODO sections with your real logic.

## Acceptance Criteria
- Transform rules are traceable back to the documented M1 quality findings.
- Any dropped columns, null-handling choices, or exception rows are written down in notes.
- Commands or outputs can be reproduced with documented steps.

## Verification
- `poetry run python local/learning-workspace/m2/week-02/src/m2_etl/transform.py`
- Review the notes that explain which rules came from M1 findings and which assumptions were newly introduced.

## Notes
Keep scope limited to this ticket and avoid jumping ahead.
## Supplemental Reading

- Docker Documentation: https://docs.docker.com/
- pandas Documentation: https://pandas.pydata.org/docs/
- Data validation (concept): https://en.wikipedia.org/wiki/Data_validation
