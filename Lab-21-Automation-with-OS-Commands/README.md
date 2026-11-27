# Lab 21 - Automation with OS Commands

## Objective
Learn how to execute Linux operating system commands using Python's subprocess module.

## Environment
- OS: Ubuntu 24.04
- Python: 3.12.3
- Module: subprocess (Python standard library)

## Concepts Learned

### 1. Running OS Commands
- Used subprocess.run() to execute Linux commands.
- Passed commands as a list of arguments.
- Used result.args to display the executed command.

### 2. Capturing Command Output
- capture_output=True captures standard output and standard error.
- text=True returns output as readable strings.
- result.stdout stores standard output.
- result.stderr stores standard error.

### 3. Checking Exit Codes
- Exit code 0 means success.
- A non-zero exit code indicates failure.
- Used result.returncode to check command status.

### 4. Handling Errors
Practised handling:
- subprocess.CalledProcessError
- FileNotFoundError
- subprocess.TimeoutExpired

Used check=True to raise an exception when a command returns a non-zero exit code.
Used timeout=1 to stop a command that takes too long.

### 5. Safe Command Execution
Commands were passed as argument lists instead of using shell=True.

## Lab Tasks
1. Execute the ls command using subprocess.
2. Capture and display stdout and stderr.
3. Check successful and unsuccessful exit codes.
4. Handle command failures, missing commands, and timeouts.

## Files
- run_ls.py: Executes ls and displays captured output.
- exitcode.py: Checks command exit codes.
- errors.py: Handles three types of subprocess errors.
- demo/: Contains sample files for testing.
- evidence/: Contains lab execution outputs.
- .gitignore: Excludes Python cache files.

## Result
All lab tasks were executed successfully.
All three Python scripts passed syntax checks.

## Learning Outcome
Learned how to automate Linux commands using Python, capture command output, check exit codes, and handle subprocess errors.
