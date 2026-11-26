# Lab 3 – Working with Variables and Data Types

## 1. Lab Overview

This lab covers Python variables, basic data types, checking data types, and type casting.

**Objectives:**
- Create variables using different data types.
- Display variable values.
- Identify data types using `type()`.
- Convert values between different data types.
- Understand invalid type conversions.

## 2. Environment Setup

**Operating System:** Ubuntu 24.04 LTS
**Python Version:** 3.12.3
**Virtual Environment:** Python venv

Commands used:

```bash
sudo apt update
sudo apt install -y python3 python3-venv

mkdir -p ~/vars-lab
cd ~/vars-lab

python3 -m venv venv
source venv/bin/activate

python3 --version
```

## 3. Task 1 – Creating Variables

Created four variables:

```python
my_integer = 10
my_float = 20.5
my_string = "Hello, World!"
my_boolean = True
```

Printed their values using `print()`.

**Output:**

```text
10
20.5
Hello, World!
True
```

## 4. Task 2 – Checking Data Types

Used the Python `type()` function:

```python
print(type(my_integer))
print(type(my_float))
print(type(my_string))
print(type(my_boolean))
```

**Output:**

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

**Data types:**

- `int`: Stores whole numbers.
- `float`: Stores decimal numbers.
- `str`: Stores text.
- `bool`: Stores True or False values.

## 5. Task 3 – Type Casting

Type casting means converting a value from one data type into another.

### A. Integer to Float

```python
new_float = float(my_integer)
print(new_float)
print(type(new_float))
```

Output:

```text
10.0
<class 'float'>
```

### B. Float to String

```python
new_string = str(my_float)
print(new_string)
print(type(new_string))
```

Output:

```text
20.5
<class 'str'>
```

### C. String to Integer

```python
another_string = "15"
new_integer = int(another_string)
print(new_integer)
print(type(new_integer))
```

Output:

```text
15
<class 'int'>
```

### D. Boolean to Integer

```python
new_integer_from_boolean = int(my_boolean)
print(new_integer_from_boolean)
```

Output:

```text
1
```

In Python:

- `True` converts to `1`.
- `False` converts to `0`.

## 6. Invalid Type Conversion Challenge

Tested an invalid conversion:

```bash
python3 -c 'int("abc")'
```

**Expected error:**

```text
ValueError: invalid literal for int() with base 10: 'abc'
```

Python raises a `ValueError` because alphabetic text cannot be converted directly into an integer.

## 7. Final Verification

Commands used:

```bash
python3 vars_types.py
python3 -m py_compile vars_types.py
python3 vars_types.py | grep -q "<class 'bool'>" && echo "bool type found"
```

**Verified results:**

- All variable values printed correctly.
- All four data types identified correctly.
- All required type conversions worked.
- Invalid conversion produced the expected `ValueError`.
- Python syntax check passed.
- Boolean type verification passed.

## 8. Project Structure

```text
Lab-03-Working-with-Variables-and-Data-Types/
│
├── README.md
├── vars_types.py
├── .gitignore
│
└── evidence/
    └── task-outputs.txt
```

## 9. Key Learning Points

1. Variables store information in Python.
2. Python supports integers, floats, strings, and booleans.
3. The `type()` function identifies a variable's data type.
4. Type casting converts values between compatible data types.
5. Invalid conversions can raise a `ValueError`.
6. Python treats `True` as `1` and `False` as `0` when converting booleans to integers.

## 10. Conclusion

Successfully completed the practical exercises for Python variables, data types, and type casting.

The lab improved understanding of how Python stores, identifies, and converts different types of data.
