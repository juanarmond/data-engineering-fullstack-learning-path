# Ticket: Create baseline tests for extract/transform/load

## Milestone
M2

## Day
D03

## Goal
Create baseline tests for extract/transform/load

## Context
This ticket is part of Week 04 progression for M2 local ETL learning.

## Tasks
- Read the ticket fully before implementation.
- Document your steps and assumptions in clear language.
- Keep outputs reproducible by another learner.
- Create tests under `local/learning-workspace/m2/week-04/tests/`.
- Cover the ETL code path already built in earlier weeks rather than introducing a separate demo pipeline.
- Create baseline automated tests for extract/transform/load.
- Include at least one failing-case test.
- Document how to run tests.

## Starter Example To Copy

```python
import unittest
import pandas as pd


class TestEtlBasics(unittest.TestCase):
    def test_example_happy_path(self) -> None:
        frame = pd.DataFrame(
            [{"Season": "2024", "Date": "2024-01-06", "Home": "A", "Away": "B"}]
        )
        self.assertEqual(len(frame), 1)

    def test_example_failing_case_placeholder(self) -> None:
        frame = pd.DataFrame([{"Season": None, "Date": "2024-01-06"}])
        self.assertTrue(frame["Season"].isna().any())
        # TODO: replace this with a real assertion about how your ETL should handle bad input.


if __name__ == "__main__":
    unittest.main()
```

Copy this into your local workspace and then replace the TODO sections with the specific behaviors from your ETL code.

## Acceptance Criteria
- Tests can be run with one documented command from the repo root.
- At least one test proves the pipeline handles a known bad or edge-case input from the M1 findings.
- Commands or outputs can be reproduced with documented steps.

## Verification
- `poetry run python -m unittest discover local/learning-workspace/m2/week-04/tests -v`
- Confirm the failing-case scenario is explained in notes, not just encoded silently in the test file.

## Notes
Keep scope limited to this ticket and avoid jumping ahead.
## Supplemental Reading

- Docker Documentation: https://docs.docker.com/
- pandas Documentation: https://pandas.pydata.org/docs/
- Data validation (concept): https://en.wikipedia.org/wiki/Data_validation
