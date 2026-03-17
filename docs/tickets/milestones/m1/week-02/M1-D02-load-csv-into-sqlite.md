# Ticket: Load CSV Into SQLite

## Milestone
M1

## Day
D02

## Goal
Move the Week 1 dummy CSV into a simple SQLite table from inside the Week 2 notebook.

## Context
This makes Week 2 feel continuous because the learner queries the same data they created in Week 1.

## Tasks
- Open `local/learning-workspace/m1/week-02/notebooks/m1_w2_sql_basics.ipynb`.
- Add `Load Dataset` and `Create Table` markdown headings.
- Load `local/learning-workspace/m1/week-01/data/dummy_matches.csv`.
- Create a SQLite database at `local/learning-workspace/m1/week-02/data/dummy_matches.db`.
- Load the CSV into a local SQLite table.
- Record the table name, source CSV path, and important columns in `local/learning-workspace/m1/week-02/notes/d02-load-plan.md`.

## Starter Snippet (One Working Way)

Use this only as a small starting point, then adapt the path and table name:

```python
from pathlib import Path
import sqlite3
import pandas as pd

csv_path = Path("local/learning-workspace/m1/week-01/data/dummy_matches.csv")
db_path = Path("local/learning-workspace/m1/week-02/data/dummy_matches.db")

df = pd.read_csv(csv_path)
conn = sqlite3.connect(db_path)
df.to_sql("dummy_matches", conn, if_exists="replace", index=False)

pd.read_sql_query("SELECT * FROM dummy_matches LIMIT 5", conn)
```

If this works, keep going and explain in your own words what each step did.

## Acceptance Criteria
- The table exists in the local database.
- The note explains what data was loaded and why.

## Verification
- Confirm the database file exists and rerun the load cells without manual fixes.
