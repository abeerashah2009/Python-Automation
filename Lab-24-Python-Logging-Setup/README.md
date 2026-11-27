# Lab 24 – Python Logging Setup

## Objective
Learn how to configure Python logging and record messages at different severity levels.

## Task 1 – Setting Up a Basic Logger
- Installed Python 3 and python3-venv.
- Created and activated a virtual environment.
- Confirmed Python version 3.12.3.
- Imported the logging module.
- Configured logging using logging.basicConfig.
- Set the logging level to DEBUG.
- Configured timestamp, level name, and message format.

## Task 2 – Logging Messages
Created four logging messages:

- DEBUG: Detailed diagnostic information.
- INFO: Confirms normal application activity.
- WARNING: Indicates an unexpected situation.
- ERROR: Reports a more serious problem.

## Task 3 – Verify Log Output
- Ran logdemo.py successfully.
- Verified all four logging levels in the console.
- Confirmed timestamps and message formatting.

## Optional Task – Write Logs to a File
- Configured logging to write to app.log.
- Used filemode='w' to overwrite previous log content.
- Verified all four messages in app.log.
- Confirmed one ERROR message and four total log messages.

## Files
- logdemo.py – Python logging script.
- app.log – Generated log output.
- evidence/task-outputs.txt – Lab verification evidence.
- .gitignore – Excludes virtual environment and Python cache files.

## Learning Outcomes
- Understand Python's logging module.
- Configure logging with basicConfig.
- Use DEBUG, INFO, WARNING, and ERROR levels.
- Write application logs to a file.
- Verify logging output.

## Conclusion
Successfully completed the Python Logging Setup lab and verified
console and file-based logging.
