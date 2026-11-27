# Lab 16 – Reading CSV Files

## 1. Objective

The objective of this lab is to understand CSV files and learn how to read, extract, and summarize data using Python's built-in `csv` module.

## 2. Environment

- Operating System: Ubuntu 24.04 LTS
- Python Version: 3.12.3
- Editor: Nano
- Python Module: csv
- Working Directory: `~/csv-lab`

## 3. Introduction to CSV Files

CSV stands for Comma-Separated Values.

A CSV file stores tabular data in plain text format. Each line represents a row, and commas separate individual fields.

CSV files are commonly used to exchange data between applications.

Example:

```csv
Name,Age,Occupation
Alice,30,Engineer
Bob,25,Data Scientist
Eve,35,Designer
```

## 4. Task 1 – Understanding CSV Files

- Learned the structure of CSV files.
- Identified rows, columns, and header fields.
- Understood how comma-separated values store tabular information.

## 5. Task 2 – Environment Setup

Commands used:

```bash
sudo apt update
sudo apt install -y python3 python3-venv nano
mkdir -p ~/csv-lab
cd ~/csv-lab
python3 -m venv venv
source venv/bin/activate
python --version
touch read_csv.py
```

Python version verified: `3.12.3`.

## 6. Task 3 – Reading CSV Files

Imported the CSV module:

```python
import csv
```

Used `open()` and `csv.reader()` to read the CSV file:

```python
with open('sample.csv', mode='r', newline='') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        print(f'Name: {row[0]}, Age: {row[1]}, Occupation: {row[2]}')
```

### Concepts learned

- `csv.reader()` reads CSV records.
- `next()` skips the header row.
- `row[0]` accesses the Name column.
- `row[1]` accesses the Age column.
- `row[2]` accesses the Occupation column.
- `newline=''` supports correct CSV line handling.

## 7. Task 4 – Summarizing CSV Data

Initialized variables:

```python
total_age = 0
row_count = 0
```

Used `csv.DictReader()` to access values by column name:

```python
with open('sample.csv', mode='r', newline='') as file:
    for row in csv.DictReader(file):
        total_age += int(row['Age'])
        row_count += 1
```

Displayed the summary:

```python
print(f'Total number of entries: {row_count}')
print(f'Total age combined: {total_age}')

if row_count > 0:
    print(f'Average age: {total_age / row_count:.2f}')
```

### Concepts learned

- `csv.DictReader()` uses header names as dictionary keys.
- `int()` converts age values into integers.
- `row_count` counts the records.
- `total_age` calculates the combined age.
- Average age is calculated from the total and record count.

## 8. Expected Results

```text
Name: Alice, Age: 30, Occupation: Engineer
Name: Bob, Age: 25, Occupation: Data Scientist
Name: Eve, Age: 35, Occupation: Designer

Total number of entries: 3
Total age combined: 90
Average age: 30.00
```

## 9. Independent Verification

Used AWK to independently calculate the number of entries, total age, and average:

```bash
awk -F, 'NR>1 {sum+=$2; n++} END {print "Entries:", n, "Total:", sum, "Average:", sum/n}' sample.csv
```

Verified output:

```text
Entries: 3 Total: 90 Average: 30
```

## 10. Verification and Testing

Python compilation:

```bash
python -m py_compile read_csv.py
```

Result: Python compilation successful.

File checks:

```bash
test -s sample.csv
test -s read_csv.py
```

Result: Both files exist and contain data.

## 11. Project Files

- `read_csv.py` – Python script for reading and summarizing CSV data.
- `sample.csv` – Sample dataset.
- `evidence/task-outputs.txt` – Practical execution evidence.
- `.gitignore` – Excludes Python cache, virtual environments, and log files.

## 12. Learning Outcome

Successfully learned how to read CSV files using Python's `csv` module, extract individual columns, skip header rows, count records, calculate numeric totals, and find averages.

This lab builds a foundation for handling structured data in Python automation and data processing tasks.
