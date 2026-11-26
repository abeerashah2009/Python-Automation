# Lab 11: File I/O Basics

## 1. Lab Overview

This lab introduces the fundamentals of File Input/Output (I/O) operations in Python.

The practical covers creating files, writing content, appending new text, and reading file contents.

**Environment:**
- Operating System: Ubuntu 24.04 LTS
- Python Version: 3.12.3
- Language: Python 3

## 2. Objectives

- Understand Python File I/O operations.
- Create and write content to a text file.
- Append additional text to an existing file.
- Read file contents using Python.
- Verify file contents and line counts.

## 3. Task 1: Create and Write to a File

### Command

```bash
python3 file_io.py
```

### Python Code

```python
# Open a file in write mode
with open('output.txt', 'w') as file:
    # Write text to the file
    file.write('Hello, World!\n')
    file.write('This is a test of file I/O.\n')
```

### Explanation

- `open()` opens a file.
- `'w'` means write mode.
- `file.write()` writes text into the file.
- If the file already exists, write mode replaces its previous content.

### Verification

```bash
cat output.txt
wc -l output.txt
```

**Expected Output:**

```text
Hello, World!
This is a test of file I/O.
2 output.txt
```

## 4. Task 2: Append Text to the File

### Python Code

```python
# Open the file in append mode
with open('output.txt', 'a') as file:
    # Append text to the file
    file.write('Appending new text.\n')
```

### Explanation

- `'a'` means append mode.
- Append mode adds new content without replacing existing content.
- `file.write()` adds the additional text.

### Verification

```bash
rm -f output.txt
python3 file_io.py
cat output.txt
wc -l output.txt
```

**Expected Output:**

```text
Hello, World!
This is a test of file I/O.
Appending new text.
3 output.txt
```

## 5. Task 3: Read From the File

### Python Code

```python
# Open the file in read mode
with open('output.txt', 'r') as file:
    # Read content from the file
    content = file.read()
    # Print the content
    print(content)
```

### Explanation

- `'r'` means read mode.
- `file.read()` reads the entire file content.
- `print()` displays the contents in the terminal.
- The `with` statement automatically closes the file after the operation.

### Verification

```bash
python3 file_io.py
cat output.txt
wc -l output.txt
```

**Expected Output:**

```text
Hello, World!
This is a test of file I/O.
Appending new text.
```

The script displays the file contents, and the `cat` command displays the saved contents again.

## 6. Complete Python Script

**File: `file_io.py`**

```python
# Open a file in write mode
with open('output.txt', 'w') as file:
    # Write text to the file
    file.write('Hello, World!\n')
    file.write('This is a test of file I/O.\n')

# Open the file in append mode
with open('output.txt', 'a') as file:
    # Append text to the file
    file.write('Appending new text.\n')

# Open the file in read mode
with open('output.txt', 'r') as file:
    # Read content from the file
    content = file.read()
    # Print the content
    print(content)
```

## 7. Important Python File Modes

| Mode | Description |
|---|---|
| `w` | Write and replace existing content |
| `a` | Append new content |
| `r` | Read existing content |

## 8. Final Verification

The following checks were successfully performed:

- Python script executed successfully.
- File creation verified.
- File writing verified.
- File appending verified.
- File reading verified.
- Output file contains exactly 3 lines.
- Python syntax compilation successful.
- Required files exist.

## 9. Conclusion

In this lab, I learned the fundamentals of file handling in Python.

I practiced creating files, writing text, appending additional content, and reading saved information.

These operations provide a foundation for data storage, file management, and Python automation.

**Lab:** 11 – File I/O Basics
**Status:** Practical tasks completed and verified.
