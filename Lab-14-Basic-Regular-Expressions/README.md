# Lab 14 – Basic Regular Expressions

## Objective
Understand regular expressions and use Python to extract phone numbers from text files.

## Environment
- Operating System: Ubuntu 24.04
- Python Version: 3.12.3
- Module: `re` (Python standard library)

## Concepts Covered
- Regular expressions (Regex)
- `re.compile()`
- `findall()`
- Pattern matching
- Lookbehind and lookahead
- Balanced parentheses
- Reading text files
- Command-line arguments
- File handling

## Task 1 – Python Installation
Installed and verified Python 3.

Command:
```bash
python3 --version
```

## Task 2 – Phone Number Matching
Created `phone_finder.py` to identify phone numbers in different formats:

- `(123) 456-7890`
- `123-456-7890`
- `123.456.7890`

Used a compiled regular expression to reject unbalanced parentheses and longer digit strings.

## Task 3 – No-Match Scenario
Tested a file containing invalid phone number patterns.

Expected result:
```text
No phone numbers found.
```

## Case Study – Customer Records
Tested phone number extraction from mixed customer records.

## Error Handling
Tested:
- Missing input filename
- Missing text file
- Invalid phone number patterns

## Files
- `phone_finder.py` – Main Python script.
- `evidence/task-outputs.txt` – Practical test results.

## Learning Outcome
Learned how to use Python regular expressions to search, extract, and validate phone number patterns from text files.
