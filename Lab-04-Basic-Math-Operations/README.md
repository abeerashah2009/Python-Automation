# Lab 04 – Basic Math Operations

## 1. Overview

This lab demonstrates how to perform basic mathematical operations using Python.

The program asks the user to enter two numbers and calculates:

- Addition
- Subtraction
- Multiplication
- Division

It also handles division by zero and invalid user input.

## 2. Environment Setup

**Operating System:** Ubuntu 24.04 LTS

**Python Version:** 3.12.3

Install Python:

```bash
sudo apt update
sudo apt install -y python3
```

Check the installed version:

```bash
python3 --version
```

## 3. Taking User Input

Python's `input()` function accepts values from the user.

The `float()` function converts the entered values into numbers. This allows both whole numbers and decimal numbers.

```python
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Error: please enter numeric values only.")
    raise SystemExit(1)
```

### Important Concepts

- `input()` – Accepts user input.
- `float()` – Converts input into a floating-point number.
- `try` – Runs code that may produce an error.
- `except ValueError` – Handles invalid numeric input.
- `SystemExit(1)` – Stops the program when input is invalid.

## 4. Performing Mathematical Operations

The program performs four basic calculations.

```python
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
```

| Operator | Operation | Example |
|---|---|---|
| `+` | Addition | 10 + 4 = 14 |
| `-` | Subtraction | 10 - 4 = 6 |
| `*` | Multiplication | 10 * 4 = 40 |
| `/` | Division | 10 / 4 = 2.5 |

## 5. Handling Division by Zero

Division by zero is not mathematically defined.

The program uses an `if/else` condition to check the second number before performing division.

```python
if num2 != 0:
    quotient_result = num1 / num2
else:
    quotient_result = "Undefined (division by zero)"
```

This prevents a `ZeroDivisionError`.

## 6. Displaying Results

The program uses f-strings to display the calculated results.

```python
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")
```

## 7. Testing the Program

### Test 1 – Normal Arithmetic

Command:

```bash
printf '10\n4\n' | python3 basic_math_operations.py
```

Expected results:

```text
Sum: 14.0
Difference: 6.0
Product: 40.0
Quotient: 2.5
```

### Test 2 – Division by Zero

Command:

```bash
printf '5\n0\n' | python3 basic_math_operations.py
```

Expected result:

```text
Quotient: Undefined (division by zero)
```

### Test 3 – Invalid Input

Command:

```bash
printf 'abc\n3\n' | python3 basic_math_operations.py
```

Expected result:

```text
Error: please enter numeric values only.
```

### Test 4 – Decimal Numbers

Command:

```bash
printf '7.5\n2.5\n' | python3 basic_math_operations.py
```

Expected results:

```text
Sum: 10.0
Difference: 5.0
Product: 18.75
Quotient: 3.0
```

### Test 5 – Python Syntax Check

Command:

```bash
python3 -m py_compile basic_math_operations.py
```

Result:

```text
Syntax check passed
```

All practical tests were completed successfully.

## 8. Project Structure

```text
Lab-04-Basic-Math-Operations/
├── .gitignore
├── README.md
├── basic_math_operations.py
└── evidence/
    └── task-outputs.txt
```

## 9. Key Learning Outcomes

After completing this lab, I learned how to:

1. Take input from users.
2. Convert input into floating-point numbers.
3. Perform addition, subtraction, multiplication and division.
4. Use conditional statements.
5. Handle division by zero.
6. Handle invalid input using exception handling.
7. Display results using f-strings.
8. Test Python programs using terminal commands.
9. Check Python syntax using `py_compile`.

## 10. Conclusion

This lab improved my understanding of Python input handling, mathematical operators, conditional statements and exception handling.

The program successfully performs basic calculations, accepts decimal numbers, handles invalid input and prevents division-by-zero errors.
