# Lab 29 - Data Manipulation with pandas (Optional)

## Objective

Learn basic data manipulation using the Python pandas library.

Read employee information from a CSV file, load it into a DataFrame, filter records based on conditions, and save the filtered data into a new CSV file.

## Environment

- OS: Ubuntu 24.04
- Python: 3.12.3
- pandas: 2.2.3
- pip: 24.0
- Virtual Environment: Python venv

## Task 1 - Setting Up the Environment

- Installed Python and python3-venv.
- Created a Python virtual environment.
- Activated the virtual environment.
- Installed pandas version 2.2.3.
- Verified the pandas installation.

## Task 2 - Reading a CSV File

Created `employees.csv` containing 10 employee records.

Columns:
- Name
- Age
- City

Used `pd.read_csv()` to load the CSV file into a pandas DataFrame.

Used `df.head()` to preview the first five records.

## Task 3 - Filtering Rows

Filtered employee records using:

`df[df['Age'] > 30]`

Results:
- Total employees: 10
- Employees older than 30: 6

## Task 4 - Saving Filtered Data

Used:

`filtered_df.to_csv('filtered_data.csv', index=False)`

Saved the six matching employee records into `filtered_data.csv`.

Verification:
- Output CSV contains 7 lines including the header.
- No employee aged 30 or below exists in the filtered output.

## Project Files

- `employees.csv` - Original employee dataset.
- `filter.py` - pandas data manipulation script.
- `filtered_data.csv` - Filtered employee records.
- `.gitignore` - Excludes Python cache and virtual environment files.
- `evidence/task-outputs.txt` - Lab execution results.

## Learning Outcomes

- Installing pandas in a Python virtual environment.
- Reading CSV files with pandas.
- Understanding DataFrames.
- Previewing data using head().
- Filtering rows using conditions.
- Saving DataFrames to CSV files.
- Excluding DataFrame indexes when exporting.

## Conclusion

Successfully completed the pandas data manipulation lab by reading employee data, filtering employees older than 30, and exporting the filtered records to a new CSV file.
