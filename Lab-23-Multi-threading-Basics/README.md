# Lab 23 - Multi-threading Basics

## Objective
Understand Python multi-threading and demonstrate concurrent execution using the threading module.

## Environment
- OS: Ubuntu 24.04
- Python: 3.12.3
- Python executable: /usr/bin/python3

## Task 1 - Introduction to Multi-threading
- Installed Python 3 and python3-venv.
- Verified Python version.
- Learned the concepts of threads and concurrency.

## Task 2 - Using the threading Module
File: threads.py

- Imported time and threading modules.
- Created a function called print_numbers().
- Printed numbers from 1 to 5 in each thread.
- Added a one-second delay using time.sleep().
- Created two threads: Thread 1 and Thread 2.
- Started both threads using start().
- Used join() to wait for both threads to finish.
- Printed a completion message.

## Task 3 - Observing Concurrency

### Multi-threaded Execution
- Executed threads.py.
- Observed interleaved output from both threads.
- Verified that all 10 count lines were printed.
- Execution time: approximately 5.048 seconds.

### Sequential Execution
File: sequential.py

- Imported print_numbers() from threads.py.
- Executed the function twice sequentially.
- Verified that all 10 count lines were printed.
- Execution time: approximately 10.045 seconds.

### Comparison
- Multi-threaded execution: 5.048 seconds.
- Sequential execution: 10.045 seconds.
- Both approaches printed 10 count lines.
- Threads overlapped their waiting time, reducing total execution time.

## Task 4 - Real-world Use Cases
- Web servers: Handle multiple client requests concurrently.
- Data processing: Perform multiple I/O operations concurrently.
- User interfaces: Keep applications responsive using background threads.

## Verification
- Python syntax check passed for both scripts.
- Threaded output count: 10.
- Sequential output count: 10.
- Both threads completed successfully.
- Evidence saved in evidence/task-outputs.txt.

## Files
- threads.py: Creates and runs two threads.
- sequential.py: Runs the same function sequentially.
- evidence/task-outputs.txt: Captured verification results.

## Learning Outcomes
- Understand threads and concurrency.
- Create and start Python threads.
- Use join() to manage thread completion.
- Observe concurrent execution.
- Compare threaded and sequential execution times.
- Identify practical multi-threading use cases.
