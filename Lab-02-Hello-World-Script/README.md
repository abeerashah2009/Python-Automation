# Lab 02 – Hello World Script

## 1. Lab Overview

This lab introduces the fundamentals of creating and running Python scripts. It demonstrates how to display text in the terminal using Python's built-in `print()` function.

**Environment:**
- Operating System: Ubuntu 24.04.5 LTS
- Python Version: 3.12.3
- Text Editor: GNU Nano 7.2
- Working Directory: `/home/ubuntu/lab`

## 2. Task 1 – Setting Up the Environment

Verified the installed Python version:

```bash
python3 --version
```

**Output:**

```text
Python 3.12.3
```

Created the working directory:

```bash
mkdir -p ~/lab
cd ~/lab
pwd
```

**Output:**

```text
/home/ubuntu/lab
```

GNU Nano was available as the terminal text editor.

## 3. Task 2 – Writing the Hello World Script

Created the Python file:

```bash
cd ~/lab
cat > hello.py <<'EOF'
# This is a simple Python script
print("Hello, World!")
EOF
```

Verified the file content:

```bash
cat hello.py
```

**Output:**

```python
# This is a simple Python script
print("Hello, World!")
```

## 4. Task 3 – Executing the Script

Executed the Python script:

```bash
cd ~/lab
python3 hello.py
```

**Output:**

```text
Hello, World!
```

Verified the exact output:

```bash
python3 hello.py | grep -x 'Hello, World!'
```

**Output:**

```text
Hello, World!
```

Checked Python syntax:

```bash
python3 -m py_compile hello.py
```

**Result:** Python syntax OK.

## 5. Project Structure

```text
Lab-02-Hello-World-Script/
├── .gitignore
├── README.md
├── hello.py
└── evidence/
    └── task-outputs.txt
```

## 6. Evidence

The `evidence/` directory contains verified terminal outputs showing:

- Ubuntu and Python versions
- Nano editor version
- Working directory
- Python script content
- Successful script execution
- Exact output verification using `grep`
- Python syntax verification

## 7. Key Concepts Learned

1. **Python Script:** A file containing Python instructions that can be executed by the Python interpreter.
2. **print() Function:** A built-in Python function used to display text or values in the terminal.
3. **Text Editor:** Nano can be used to create and edit files directly from the terminal.
4. **Command Line:** Commands such as `cd`, `cat`, and `python3` help manage and execute Python files.
5. **Syntax Verification:** `py_compile` checks whether a Python file can be compiled successfully.

## 8. Conclusion

Successfully created and executed the first Hello World Python script on Ubuntu 24.04.5 LTS. Verified the exact console output and confirmed that the Python file passed the syntax check.

This lab provided practical experience with Python scripts, the `print()` function, Nano, and command-line execution.
