# Lab 09 – Working with Lists and Tuples

## 1. Overview

This lab explains two important Python data structures: Lists and Tuples.

Lists are mutable, which means their elements can be changed after creation. Tuples are immutable, which means their elements cannot be changed after creation.

## 2. Learning Objectives

- Create and print Python lists.
- Add elements to a list.
- Remove elements from a list.
- Sort list elements.
- Create and use tuples.
- Understand tuple immutability.
- Differentiate between lists and tuples.

## 3. Environment

- Operating System: Ubuntu 24.04
- Python Version: 3.12.3
- Virtual Environment: venv
- Python Library: Standard Library

Check Python version:

```bash
python3 --version
```

Activate the virtual environment:

```bash
source ~/lists-tuples-lab/venv/bin/activate
```

## 4. Task 1 – Creating and Printing a List

A list is an ordered and mutable collection of elements.

### Code

```python
# Task 1: create and print a list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("The list of fruits is:", fruits)
```

### Output

```text
The list of fruits is: ['apple', 'banana', 'cherry', 'date', 'elderberry']
```

### Explanation

- A list is created using square brackets `[]`.
- Items are separated by commas.
- A list can store multiple values.
- List elements can be modified after creation.

## 5. Task 2 – Modifying the List

Python provides built-in methods to modify lists.

### Code

```python
fruits.append("fig")
print("After adding 'fig':", fruits)

fruits.remove("date")
print("After removing 'date':", fruits)

fruits.sort()
print("The sorted list of fruits is:", fruits)
```

### Output

```text
After adding 'fig': ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
After removing 'date': ['apple', 'banana', 'cherry', 'elderberry', 'fig']
The sorted list of fruits is: ['apple', 'banana', 'cherry', 'elderberry', 'fig']
```

### Explanation

**append()**

Adds a new element at the end of a list.

**remove()**

Removes the specified element from a list.

**sort()**

Arranges list elements in ascending order.

## 6. Task 3 – Demonstrating Tuple Immutability

A tuple is an ordered and immutable collection of elements.

### Code

```python
fruit_tuple = ("apple", "banana", "cherry", "elderberry", "fig")
print("The tuple is:", fruit_tuple)

try:
    fruit_tuple[0] = "avocado"
except TypeError as e:
    print(f"TypeError caught: {e}")
```

### Output

```text
The tuple is: ('apple', 'banana', 'cherry', 'elderberry', 'fig')
TypeError caught: 'tuple' object does not support item assignment
```

### Explanation

- A tuple is created using parentheses `()`.
- Tuple elements cannot be reassigned.
- Attempting to modify an element raises a `TypeError`.
- The `try` and `except` blocks catch and display the error.

## 7. Difference Between Lists and Tuples

| Feature | List | Tuple |
|---|---|---|
| Brackets | Square `[]` | Parentheses `()` |
| Mutability | Mutable | Immutable |
| Modification | Elements can be changed | Elements cannot be reassigned |
| Methods | append(), remove(), sort() | count(), index() |
| Use | Data that may change | Data that should remain fixed |

## 8. Important Python Concepts

**Mutability:** The ability of an object to be changed after creation.

**Immutability:** The inability to change an object's elements after creation.

**append():** Adds an element to the end of a list.

**remove():** Removes a specified element from a list.

**sort():** Sorts list elements in ascending order.

**TypeError:** An exception raised when an operation is applied to an object of an inappropriate type.

## 9. Verification Commands

Run the complete Python script:

```bash
python3 lists_tuples.py
```

Verify tuple immutability:

```bash
python3 lists_tuples.py 2>&1 | grep -q 'TypeError' && echo "TypeError found"
```

Verify list sorting:

```bash
python3 lists_tuples.py | grep -q 'sorted list' && echo "sorted list found"
```

Expected verification output:

```text
TypeError found
sorted list found
```

## 10. Project Structure

```text
Lab-09-Working-with-Lists-and-Tuples/
│
├── .gitignore
├── README.md
├── lists_tuples.py
│
└── evidence/
    └── task-outputs.txt
```

## 11. Conclusion

In this lab, I learned how to create, print, modify, and sort Python lists. I also created a tuple and demonstrated its immutability by attempting to change one of its elements.

This practical helped me understand the difference between mutable lists and immutable tuples and when to use each data structure in Python programming.

## 12. Evidence

The `evidence/task-outputs.txt` file contains the practical outputs for all three tasks and the required verification results.
