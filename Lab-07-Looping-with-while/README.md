# Lab 07 – Looping with `while`

## 1. Overview

This lab demonstrates how to use Python `while` loops to repeat instructions while a condition is true. It also covers interactive input, stopping a loop with a specific word, handling `EOFError`, and using `finally` for graceful program termination.

## 2. Objectives

- Understand how a `while` loop works.
- Repeat statements while a condition remains true.
- Accept input from the user inside a loop.
- Stop a loop when the user enters `exit`.
- Handle `EOFError` safely.
- Use `try` and `finally` to perform cleanup or display a final message.

## 3. Environment

- Operating system: Ubuntu 24.04
- Python version: 3.12.3
- Repository: Python-Automation

## 4. Understanding the While Loop

A `while` loop repeats a block of code as long as its condition is true.

General syntax:

```python
while condition:
    # statements to repeat
```

The condition must eventually become false, or the loop must be stopped with a `break` statement.

## 5. Task 1 – Count from 1 to 5

### Code: `count.py`

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

### Explanation

1. The variable `count` starts at 1.
2. The loop checks whether `count` is less than or equal to 5.
3. `print(count)` displays the current number.
4. `count += 1` increases the number by one.
5. The loop stops when `count` becomes 6.

### Run the program

```bash
python3 count.py
```

### Expected output

```text
1
2
3
4
5
```

## 6. Task 2 – Interactive While Loop

The program repeatedly asks the user to enter a string. It stops when the user types `exit`.

### Code: `while_loop.py` (Task 2 version)

```python
user_input = ''

while True:
    try:
        user_input = input("Enter a string (type 'exit' to quit): ")
    except EOFError:
        print("\nInput ended.")
        break

    if user_input == "exit":
        break

    print("You entered:", user_input)
```

### Explanation

- `while True` creates a loop that continues until stopped.
- `input()` asks the user for a string.
- `if user_input == "exit"` checks whether the user wants to quit.
- `break` stops the loop.
- `except EOFError` handles the end of input without an unexpected crash.

### Test the exit condition

```bash
printf 'a\nb\nexit\n' | python3 while_loop.py
```

The program displays the entered strings and stops when it receives `exit`.

### Test EOFError

```bash
printf 'a\n' | python3 while_loop.py
```

The program handles the end of input and displays `Input ended.`

## 7. Task 3 – Graceful Termination with Finally

The final version extends Task 2 by displaying a goodbye message and using `finally` to display a termination message.

### Final code: `while_loop.py`

```python
user_input = ''

try:
    while True:
        try:
            user_input = input("Enter a string (type 'exit' to quit): ")
        except EOFError:
            print("\nInput ended.")
            break

        if user_input == "exit":
            print("Exiting the loop. Goodbye!")
            break

        print("You entered:", user_input)

finally:
    print("Program terminated successfully.")
```

### Explanation

- The outer `try` block contains the loop.
- The inner `try` block handles input.
- `break` stops the loop when `exit` is entered or EOF occurs.
- `finally` runs when control leaves the `try` block, including after either normal exit or handled EOF.
- The final message confirms that the program has terminated.

### Test normal exit

```bash
printf 'a\nb\nexit\n' | python3 while_loop.py
```

Expected ending:

```text
Exiting the loop. Goodbye!
Program terminated successfully.
```

### Test EOFError with finally

```bash
printf 'a\n' | python3 while_loop.py
```

Expected ending:

```text
Input ended.
Program terminated successfully.
```

## 8. Python Syntax Validation

Run:

```bash
python3 -m py_compile count.py while_loop.py
```

Result:

```text
Syntax validation passed.
```

## 9. Project Structure

```text
Lab-07-Looping-with-while/
├── .gitignore
├── README.md
├── count.py
├── while_loop.py
└── evidence/
    └── task-outputs.txt
```

## 10. Key Concepts Learned

| Concept | Purpose |
|---|---|
| `while` | Repeats code while a condition is true |
| `while True` | Creates a loop that continues until stopped |
| `break` | Exits a loop |
| `input()` | Accepts user input |
| `EOFError` | Handles input ending unexpectedly |
| `try` | Wraps code that may raise an exception |
| `finally` | Runs when the `try` block is exited |

## 11. Conclusion

In this lab, I practised Python `while` loops, counting, interactive input, exit conditions, EOFError handling, and graceful termination using `finally`. Both Python programs passed syntax validation, and the expected test outputs were verified.

## 12. Evidence

See `evidence/task-outputs.txt` for the recorded commands and test outputs.
