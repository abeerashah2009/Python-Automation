# Lab 05 – Conditional Statements (`if`, `elif`, `else`)

## 1. Overview

This lab demonstrates how to use conditional statements in Python to compare two numbers.

The program accepts two numbers through command-line arguments and determines which number is larger or whether both numbers are equal.

## 2. Objectives

- Understand Python conditional statements.
- Use `if`, `elif`, and `else`.
- Read command-line arguments using `sys.argv`.
- Convert input values into integers.
- Compare two numbers.
- Test greater-than, less-than, and equal conditions.

## 3. Environment

- Operating System: Ubuntu 24.04 LTS
- Python Version: 3.12.3
- Editor: Nano
- Terminal: Ubuntu

## 4. Understanding Conditional Statements

Python provides conditional statements to make decisions.

- `if`: Executes code when a condition is true.
- `elif`: Checks another condition when the previous condition is false.
- `else`: Executes when all previous conditions are false.

## 5. Reading Command-Line Arguments

The program uses:

```python
import sys

number1 = int(sys.argv[1])
number2 = int(sys.argv[2])
```

- `sys.argv[1]` reads the first number.
- `sys.argv[2]` reads the second number.
- `int()` converts the arguments into integers.

## 6. Python Program

File: `compare.py`

```python
import sys

# Read two numbers from the command line
number1 = int(sys.argv[1])
number2 = int(sys.argv[2])

# Conditional statements with elif
if number1 > number2:
    print("Number 1 is larger")
elif number1 < number2:
    print("Number 2 is larger")
else:
    print("Both numbers are equal")
```

## 7. Running the Program

Move into the lab directory:

```bash
cd ~/Python-Automation/Lab-05-Conditional-Statements
```

Run the program with different values:

```bash
python3 compare.py 10 20
python3 compare.py 30 20
python3 compare.py 10 10
```

## 8. Test Results

| Test | Input | Expected Output |
|---|---|---|
| Number 2 is larger | `10 20` | Number 2 is larger |
| Number 1 is larger | `30 20` | Number 1 is larger |
| Equal numbers | `10 10` | Both numbers are equal |
| Number 1 is larger | `30 20` | Number 1 is larger |
| Number 2 is larger | `15 25` | Number 2 is larger |
| Equal numbers | `50 50` | Both numbers are equal |

All listed test cases passed.

## 9. Python Syntax Check

Command:

```bash
python3 -m py_compile compare.py
```

Result:

```text
Syntax check passed
```

## 10. Project Structure

```text
Lab-05-Conditional-Statements/
├── .gitignore
├── README.md
├── compare.py
└── evidence/
    └── task-outputs.txt
```

## 11. Key Concepts Learned

- Python conditional statements
- `if`, `elif`, and `else`
- Command-line arguments
- Integer conversion using `int()`
- Comparison operators (`>`, `<`)
- Testing different conditions
- Python syntax validation

## 12. Conclusion

In this lab, I created and tested a Python program using conditional statements. The program correctly identifies which of two numbers is larger and handles equal numbers using `if`, `elif`, and `else`.
