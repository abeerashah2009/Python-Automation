# Lab 13 – Command-Line Arguments

## Objective
Understand how to pass, access, and handle command-line arguments in Python.

## Concepts Covered
- Command-line arguments
- `sys.argv`
- `argparse` module
- Positional arguments
- Optional arguments
- Default values
- Type checking
- Automatic help messages
- Handling missing arguments

## Task 1 – Access Arguments Using sys.argv
Created `sys_args_demo.py` to read command-line arguments using the `sys` module.

Example:
```bash
python3 sys_args_demo.py hello 42 world
```

## Task 2 – Handle No Arguments
Added a condition to detect when no command-line arguments are provided.

Example:
```bash
python3 sys_args_demo.py
```

## Task 3 – Parse Arguments Using argparse
Created `args_demo.py` using `argparse.ArgumentParser`.

- `name`: Required positional string argument.
- `--age`: Optional integer argument.
- Default age: 25.

Example:
```bash
python3 args_demo.py John --age 30
```

Output:
```text
Name: John
Age: 30
```

## Additional Tests
- Tested default age without `--age`.
- Tested invalid age input.
- Tested missing required name.
- Tested automatic `--help` output.
- Verified both Python scripts compile successfully.

## Files
- `sys_args_demo.py` – Demonstrates sys.argv.
- `args_demo.py` – Demonstrates argparse.
- `evidence/task-outputs.txt` – Practical test results.

## Learning Outcome
Learned how to accept command-line inputs, process positional and optional arguments, set default values, and handle invalid or missing arguments.
