# Lab 25 – Creating a Simple CLI with argparse

## Objective
Understand how to create a command-line interface using Python's argparse module.

## Task 1 – Environment Setup
- Installed Python 3 on Ubuntu 24.04.
- Confirmed Python version 3.12.3.
- Used argparse from Python's standard library; no external installation required.

## Task 2 – Basic CLI
- Imported argparse.
- Created an ArgumentParser with a description.
- Added --verbose as a store_true flag.
- Added --file to accept a file path.
- Parsed command-line arguments.
- Tested both options together using example.txt.

## Task 3 – Enhanced CLI
- Added --level as an integer option.
- Restricted --level to choices 1, 2, and 3.
- Verified valid input with --level 2.
- Verified invalid input with --level 5; argparse returned exit code 2.
- Added --timeout with a default value of 30 seconds.
- Tested custom timeout value of 10 seconds.
- Tested combined options.
- Verified automatically generated --help output.

## Files
- cli_example.py – CLI application.
- example.txt – Sample input file.
- evidence/task-outputs.txt – Command outputs and test evidence.
- .gitignore – Excludes Python cache files.

## Learning Outcomes
- Understand ArgumentParser and add_argument.
- Use boolean flags and string arguments.
- Validate integer arguments with choices.
- Configure default argument values.
- Use automatic help and error handling.

## Conclusion
Successfully created and tested a command-line interface using argparse.
The CLI supports verbose output, file paths, restricted levels, and timeout defaults.
