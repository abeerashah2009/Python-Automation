# Lab 15 – Date and Time Operations

## 1. Objective

The objective of this lab is to understand how to work with dates and times in Python using the `datetime` module.

## 2. Environment

- Operating System: Ubuntu 24.04
- Python Version: 3.12.3
- Python Module: `datetime`
- Working Directory: `~/datetime-lab`

## 3. Concepts Covered

- Python `datetime` module
- Current local date and time
- UTC (Coordinated Universal Time)
- Naive and timezone-aware datetime objects
- `datetime.now()`
- `timezone.utc`
- `timedelta`
- Date arithmetic
- `strftime()`
- Date and time formatting
- Python assertions

## 4. Task 1 – Getting Current Date and Time

Used the `datetime` module to retrieve the current date and time.

**Local date and time:**

```python
current_datetime = datetime.now()
```

**UTC date and time:**

```python
utc_datetime = datetime.now(timezone.utc)
```

### Learning Notes

- `datetime.now()` returns the current local date and time.
- A naive datetime object does not contain timezone information.
- `datetime.now(timezone.utc)` returns a timezone-aware UTC datetime.
- UTC output includes the `+00:00` timezone offset.

## 5. Task 2 – Calculating Yesterday and Next Week

Used a fixed date for predictable calculations:

```python
fixed = datetime(2026, 1, 15, 10, 30)
```

**Calculate yesterday:**

```python
yesterday = fixed - timedelta(days=1)
```

**Calculate next week:**

```python
next_week = fixed + timedelta(weeks=1)
```

### Expected Results

- Yesterday: `2026-01-14 10:30:00`
- Next week: `2026-01-22 10:30:00`

### Learning Notes

- `timedelta(days=1)` represents one day.
- `timedelta(weeks=1)` represents one week.
- We can add or subtract a `timedelta` from a datetime object.
- Assertions help verify expected calculation results.

## 6. Task 3 – Formatting Dates and Times

Used `strftime()` to convert a datetime object into a formatted string.

```python
formatted_datetime = fixed.strftime("%Y-%m-%d %H:%M:%S")
```

### Format Codes

| Code | Meaning |
|---|---|
| `%Y` | Four-digit year |
| `%m` | Two-digit month |
| `%d` | Day of the month |
| `%H` | Hour (24-hour format) |
| `%M` | Minute |
| `%S` | Second |

**Expected result:**

```text
2026-01-15 10:30:00
```

## 7. Verification and Testing

The following checks were completed:

- Python version verified.
- Python syntax compilation passed.
- Local and UTC date/time retrieved.
- Yesterday calculation verified.
- Next week's date calculation verified.
- Date formatting verified.
- Calculation assertions passed.
- Formatting assertion passed.

## 8. Project Files

- `dates.py` – Main Python script containing all three tasks.
- `evidence/task-outputs.txt` – Practical test results and verification notes.
- `.gitignore` – Excludes Python cache and unnecessary files.

## 9. Learning Outcome

After completing this lab, I learned how to:

1. Retrieve the current local date and time.
2. Retrieve timezone-aware UTC date and time.
3. Calculate past and future dates using `timedelta`.
4. Format datetime objects using `strftime()`.
5. Verify expected results using Python assertions.

These skills are useful in automation scripts, logging systems, scheduling applications, and other software projects.
