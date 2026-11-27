# Lab 17 - Writing CSV Files

## 1. Objective

The objective of this lab is to learn how to create and write CSV
(Comma-Separated Values) files using Python's built-in csv module.

## 2. Environment

- Operating System: Ubuntu 24.04 LTS
- Python Version: 3.12.3
- Editor: Nano
- Python Module: csv

## 3. Concepts Learned

### CSV Module

Python provides a built-in csv module for reading and writing
CSV files.

### csv.writer()

- Used to write rows into a CSV file.
- Accepts data in list or tuple format.
- The writerow() method writes one row at a time.

### csv.DictWriter()

- Used to write dictionary data into a CSV file.
- Uses fieldnames to define column headings.
- The writeheader() method writes the header row.
- The writerow() method writes dictionary records.

### newline=''

Using newline='' when opening a CSV file helps prevent
unwanted blank lines.

## 4. Practical Tasks

### Task 1 - Prepare Data

Created:
- A list of dictionaries named data_dict.
- A list of tuples named data_tuple.

Both contain Name, Age, and City information.

### Task 2 - Write CSV Using csv.writer()

Created people.csv using csv.writer().

### Task 3 - Write CSV Using csv.DictWriter()

Created people_dict.csv using csv.DictWriter().

## 5. Commands Used

Check Python version:

    python --version

Compile the Python script:

    python3 -m py_compile write_csv.py

Execute the script:

    python write_csv.py

Display CSV content:

    cat people.csv

Format CSV output:

    column -s, -t people.csv

Search for a specific row:

    grep -q 'Alice,28,New York' people.csv

Count CSV rows:

    python -c "import csv; print(sum(1 for _ in csv.reader(open('people.csv'))))"

Compare both CSV files:

    diff people.csv people_dict.csv

## 6. Expected CSV Output

    Name,Age,City
    Alice,28,New York
    Bob,34,Chicago
    Charlie,22,San Francisco

## 7. Verification Results

- Python syntax compilation successful.
- Both CSV files created successfully.
- CSV content displayed correctly.
- Alice's record found successfully.
- Total CSV rows: 4 (including header).
- Both CSV files contain identical data.

## 8. Project Files

- write_csv.py - Python script for writing CSV files.
- people.csv - CSV file created using csv.writer().
- people_dict.csv - CSV file created using csv.DictWriter().
- evidence/ - Practical execution and verification evidence.

## 9. Learning Outcome

I learned how to create CSV files using Python's csv module,
write records using csv.writer() and csv.DictWriter(),
and verify CSV data using Linux commands.
