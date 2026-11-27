# Lab 28 - File and Directory Cleanup Script

## Objective

Create a Python script to identify and remove files older than a specified number of days.

The script uses a safe dry-run mode by default and requires an explicit option to delete files.

## Environment

- OS: Ubuntu 24.04
- Python: 3.12.3
- Modules: argparse, logging, time, pathlib

## Task 1 - Create Test Files

Created a test directory at:

`~/FileCleanupLab/test_directory`

Created three old files and two recent files to test the cleanup process.

## Task 2 - Develop the Cleanup Script

Created `cleanup_script.py` with these features:

- Accepts a directory and age threshold as command-line arguments.
- Identifies files older than the specified number of days.
- Uses dry-run mode by default.
- Deletes files only when `--apply` is specified.
- Logs cleanup activity.
- Rejects directories outside `~/FileCleanupLab`.
- Processes files in the specified directory without recursive deletion.

## Task 3 - Dry Run and Safety Check

Ran the script with a 30-day threshold.

- Identified exactly three old files.
- Preserved all five files during the dry run.
- Correctly rejected `/tmp` as an unsafe directory.

## Task 4 - Apply Cleanup

Ran the script with the `--apply` option.

- Deleted `old1.log`.
- Deleted `old2.log`.
- Deleted `old3.txt`.
- Preserved `recent1.txt` and `recent2.txt`.

## Task 5 - Logging

The script writes activity to:

`~/FileCleanupLab/cleanup_log.txt`

Verified that the log contains exactly three `Deleted:` entries.

## Project Files

- `cleanup_script.py` - Main cleanup program.
- `.gitignore` - Excludes Python cache and virtual environment files.
- `evidence/task-outputs.txt` - Lab execution results.
- `README.md` - Lab documentation.

## Learning Outcomes

- Working with Python file and directory operations.
- Calculating file age using timestamps.
- Building command-line interfaces with argparse.
- Implementing safe dry-run behavior.
- Using logging to record file operations.
- Applying directory validation before deletion.

## Conclusion

Successfully created and tested a file cleanup script with dry-run protection, directory safety validation, actual file deletion, and logging.
