# Lab 06 – Looping with `for` in Python

## 1. Overview

This lab demonstrates how to use Python `for` loops to repeat instructions and process sequences of data.

The program prints numbers from 1 to 5, iterates through a list of fruits, and counts the total number of items processed.

## 2. Objectives

- Understand Python `for` loops.
- Use the `range()` function.
- Iterate over lists.
- Understand the `enumerate()` function.
- Count items processed during iteration.
- Display a summary using an f-string.

## 3. Environment

- Operating System: Ubuntu 24.04 LTS
- Python Version: 3.12.3
- Editor: Nano
- Terminal: Ubuntu

## 4. Understanding the for Loop

A `for` loop repeats a block of code for each item in a sequence.

General syntax:

```python
for item in sequence:
    print(item)
```

The loop processes each item one by one.

## 5. Task 1 – Print Numbers from 1 to 5

The `range()` function generates a sequence of numbers.

Code:

```python
for number in range(1, 6):
    print(number)
```

Command:

```bash
python3 for_loops.py
```

Output:

```text
1
2
3
4
5
```

Explanation:

- `range(1, 6)` starts at 1.
- The ending value 6 is excluded.
- The loop prints each number.

## 6. Task 2 – Loop Through a List of Strings

A Python list stores multiple items in an ordered collection.

Code:

```python
fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    print(fruit)
```

Output:

```text
apple
banana
cherry
date
```

Explanation:

The loop accesses each fruit in the list and prints it in the original order.

## 7. Optional – Using enumerate()

The `enumerate()` function provides both the position and the item during iteration.

Command:

```bash
python3 -c 'for i, f in enumerate(["apple", "banana"], start=1): print(i, f)'
```

Output:

```text
1 apple
2 banana
```

Explanation:

- `i` represents the item number.
- `f` represents the fruit.
- `start=1` starts numbering from 1.

## 8. Task 3 – Count Processed Items

A counter variable can track how many items are processed in a loop.

Code:

```python
item_count = 0

for fruit in fruits:
    item_count += 1
    print(fruit)

print(f"Total number of items processed: {item_count}")
```

Output:

```text
apple
banana
cherry
date
Total number of items processed: 4
```

Explanation:

- `item_count = 0` initializes the counter.
- `item_count += 1` increases the counter by one during each iteration.
- The final statement displays the total.

## 9. Complete Python Program

File: `for_loops.py`

```python
for number in range(1, 6):
    print(number)

fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(fruit)

item_count = 0
for fruit in fruits:
    item_count += 1
    print(fruit)

print(f"Total number of items processed: {item_count}")
```

## 10. Verification and Test Results

| Test | Expected Result | Status |
|---|---|---|
| Print numbers | 1 to 5 | Passed |
| Iterate through fruits | 4 fruit names | Passed |
| Use enumerate() | Numbered fruit items | Passed |
| Count processed items | 4 | Passed |
| Total output lines | 14 | Passed |
| Python syntax check | No syntax errors | Passed |

Verification commands:

```bash
python3 for_loops.py | grep -c .
python3 for_loops.py | grep "Total"
python3 -m py_compile for_loops.py
```

## 11. Project Structure

```text
Lab-06-Looping-with-for/
├── .gitignore
├── README.md
├── for_loops.py
└── evidence/
    └── task-outputs.txt
```

## 12. Key Concepts Learned

- `for` loops
- `range()` function
- Iterating over lists
- `enumerate()` function
- Counter variables
- Increment operator (`+=`)
- f-strings
- Python syntax validation

## 13. Conclusion

In this lab, I practiced Python `for` loops by printing a numerical range, processing a list of fruits, and counting the number of processed items.

I also explored `enumerate()` to display item positions and verified the program using Python syntax checks.
