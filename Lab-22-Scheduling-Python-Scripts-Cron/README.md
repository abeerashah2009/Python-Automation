# Lab 22 - Scheduling Python Scripts with Cron

## Objective
Learn how to schedule Python scripts automatically using cron on Ubuntu.

## Environment
- OS: Ubuntu 24.04
- Python: 3.12.3
- Python executable: /usr/bin/python3
- Scheduler: cron

## Python Script
File: time_logger.py

- Imported datetime and pathlib modules.
- Created a log file at ~/cron_lab/log.txt.
- Used the current date and time.
- Appended timestamps to the log file.
- Used a main guard to execute the function.

## Cron Scheduling
- Checked that cron was installed and active.
- Created a cron job to run the Python script every minute.
- Used absolute paths for Python and the script.
- Redirected output and errors to cron.err.
- Verified the scheduled job using crontab -l.
- Checked cron execution through system journal logs.

## Cron Expression

* * * * *

- Minute: Every minute
- Hour: Every hour
- Day of month: Every day
- Month: Every month
- Day of week: Every day

## Verification Results
- Python syntax check passed.
- Manual script execution succeeded.
- Cron automatically generated timestamps.
- Verified execution at 09:54 and 09:55.
- Timestamp log contained three entries.
- No cron errors were reported.
- Removed the test cron entry after successful verification.

## Evidence
- evidence/cron-log.txt
- evidence/task-outputs.txt

## Learning Outcomes
- Understand cron scheduling.
- Create recurring cron jobs.
- Schedule Python scripts automatically.
- Use absolute paths in cron commands.
- Verify scheduled execution using logs.
