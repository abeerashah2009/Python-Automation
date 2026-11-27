# Lab 26 – Reading Excel Files (Optional)

## Objective
Learn how to read Excel workbooks, access cell values, iterate through rows, and summarize spreadsheet data using Python and openpyxl.

## Task 1 – Install Required Libraries
- Updated Ubuntu package lists.
- Installed Python 3, python3-venv, and unzip.
- Created and activated a Python virtual environment.
- Installed openpyxl version 3.1.5.
- Verified the installed package version.

## Task 2 – Create and Open Excel File
- Created make_xlsx.py using the openpyxl Workbook class.
- Generated sample.xlsx.
- Created a worksheet named Sales.
- Added sample sales data.
- Verified the workbook structure using unzip.
- Loaded the workbook using openpyxl.load_workbook().
- Confirmed the active worksheet name.

## Task 3 – Read Cell Values
- Accessed cell A1 using sheet['A1'].value.
- Retrieved spreadsheet rows using iter_rows().
- Used values_only=True to read cell values directly.

## Task 4 – Data Transformation and Summarization
- Iterated over column B, skipping the header.
- Calculated the sum of numeric values.
- Verified the result was 42.

## Formula Handling Challenge
- Created a formula workbook using openpyxl.
- Added the formula =SUM(A1:A2).
- Confirmed normal loading returns the formula text.
- Confirmed data_only=True returns None because openpyxl does not calculate formulas or generate cached results.

## Files
- make_xlsx.py – Creates the sample Excel workbook.
- read_xlsx.py – Reads cells and summarizes spreadsheet data.
- sample.xlsx – Sample Sales workbook.
- formula.xlsx – Formula handling example.
- evidence/task-outputs.txt – Lab command outputs.
- .gitignore – Excludes virtual environment and Python cache files.

## Learning Outcomes
- Install and use openpyxl.
- Create and load Excel workbooks.
- Access individual cells and iterate over rows.
- Perform basic data summarization.
- Understand how formula values and cached results are handled.

## Conclusion
Successfully completed the Excel reading exercises using Python and openpyxl.
All tasks and the formula handling challenge were tested successfully.
