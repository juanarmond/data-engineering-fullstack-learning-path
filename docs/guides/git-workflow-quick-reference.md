# Git Workflow Quick Reference

## Daily Flow

```bash
git status
git branch --show-current
git pull --rebase
```

## Create a Branch

```bash
git checkout -b docs/m1-ticket-updates
```

## Stage and Commit

```bash
git add docs/tickets/milestones/m1/week-02/README.md
git commit -m "docs(m1): require notebook section headings"
```

## Push

```bash
git push -u origin docs/m1-ticket-updates
```

## Review Changes

```bash
git diff
git diff --staged
git log --oneline -n 10
```

## Safe Undo Patterns

```bash
git restore --staged <file>
git checkout -- <file>   # use only if you intentionally want to discard local edits
```
