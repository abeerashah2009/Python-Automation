# Lab 10 – Dictionary Operations

## 1. Overview

This lab covers basic dictionary operations in Python.

A dictionary stores data in key-value pairs. Each key is used to access its corresponding value.

## 2. Learning Objectives

- Create a Python dictionary.
- Understand dictionary keys and values.
- Retrieve values using keys.
- Update existing dictionary values.
- Add new key-value pairs.
- Verify dictionary operations using assertions.

## 3. Environment

- Operating System: Ubuntu 24.04
- Python Version: 3.12.3
- Editor: Nano
- Script: `dict_ops.py`

## 4. Task 1 – Create a Dictionary

A dictionary named `person_info` was created with three key-value pairs.

### Code

```python
person_info = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

print("Created:", person_info)
```

### Output

```text
Created: {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

### Explanation

- `name`, `age`, and `city` are dictionary keys.
- `Alice`, `30`, and `New York` are their values.
- Python dictionaries preserve insertion order.

## 5. Task 2 – Retrieve a Value by Key

The value associated with the `name` key was retrieved.

### Code

```python
name_value = person_info['name']
print("Name:", name_value)
```

### Output

```text
Name: Alice
```

### Explanation

Square brackets are used to access a dictionary value through its key.

## 6. Task 3 – Update and Add Dictionary Values

The existing age value was updated from 30 to 31. A new occupation key was added.

### Code

```python
person_info['age'] = 31

person_info['occupation'] = 'Engineer'

print("Updated Dictionary:", person_info)
```

### Output

```text
Updated Dictionary: {'name': 'Alice', 'age': 31, 'city': 'New York', 'occupation': 'Engineer'}
```

## 7. Assertion Verification

The `assert` statement was used to check that the age was updated and the occupation key was added.

### Code

```python
assert person_info['age'] == 31 and 'occupation' in person_info
print("Checks passed")
```

### Output

```text
Checks passed
```

## 8. Important Python Concepts

| Concept | Explanation |
|---|---|
| Dictionary | Stores key-value pairs |
| Key | Used to access a value |
| Value | Information stored against a key |
| Retrieve | Access a value using its key |
| Update | Change an existing value |
| Add | Insert a new key-value pair |
| Assert | Verify whether a condition is true |

## 9. Complete Script Execution

Run the complete lab using:

```bash
python3 dict_ops.py
```

Expected output:

```text
Created: {'name': 'Alice', 'age': 30, 'city': 'New York'}
Name: Alice
Updated Dictionary: {'name': 'Alice', 'age': 31, 'city': 'New York', 'occupation': 'Engineer'}
Checks passed
```

## 10. Project Structure

```text
Lab-10-Dictionary-Operations/
├── .gitignore
├── README.md
├── dict_ops.py
└── evidence/
    └── task-outputs.txt
```

## 11. Conclusion

In this lab, I learned how to create and manage Python dictionaries.

I successfully created a dictionary, retrieved a value using its key, updated an existing value, and added a new key-value pair.

I also used an assertion to verify the dictionary operations.

All three practical tasks were completed and verified.

## 12. Evidence

Practical outputs and verification results are saved in:

`evidence/task-outputs.txt`
