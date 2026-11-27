# Lab 30 - Final Automation Project Example

## Objective
Build a Python automation workflow to fetch data from a public API, process records, save results to CSV, and implement logging, error handling, and CLI arguments.

## Environment
- OS: Ubuntu 24.04
- Python: 3.12.3
- Requests: 2.32.3
- Virtual environment: `.venv`
- API: JSONPlaceholder

## Task 1 - Fetching Data
- Used the JSONPlaceholder posts API.
- Implemented `fetch_posts()` using the Requests library.
- Configured a 10-second request timeout.
- Used `raise_for_status()` for HTTP error handling.
- Successfully fetched 100 records.
- Configured the trusted system CA bundle for HTTPS certificate verification.

## Task 2 - Processing Data
- Implemented `process_posts(data, user_id)`.
- Extracted `userId` and `title`.
- Filtered records by user ID.
- Verified 10 posts for User 1.

## Task 3 - CSV Output
- Implemented `write_csv()`.
- Saved processed records to `user_posts.csv`.
- Used `csv.DictWriter`.
- Used `newline=""` and included the CSV header.
- Verified 11 lines for 10 records.

## Task 4 - Logging and Error Handling
- Configured Python logging.
- Logged successful API fetching.
- Logged request failures.
- Used `sys.exit(1)` when an API request fails.

## Task 5 - CLI Arguments
- Implemented `argparse`.
- Added the `--user_id` argument.
- Default user ID is 1.
- Tested User 1 and User 2 successfully.
- Both users returned 10 posts.

## Project Files
- `automation.py` - Main automation script.
- `user_posts.csv` - Generated CSV output.
- `evidence/task-outputs.txt` - Verification evidence.
- `.gitignore` - Excluded generated and environment files.

## Learning Outcomes
- API requests and JSON processing.
- Python functions and list comprehensions.
- CSV file writing.
- Logging and exception handling.
- Command-line argument parsing.
- Virtual environment management.

## Conclusion
Successfully developed and tested an end-to-end Python automation workflow using an external API, data processing, CSV output, logging, error handling, and CLI arguments.
