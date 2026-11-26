# Lab 08 – Creating and Using Functions

## 1. Overview

This lab covers how to create, define, call, and reuse functions in Python.

Functions help divide a program into smaller, reusable parts. They make code easier to understand, test, and maintain.

## 2. Learning Objectives

- Define and call Python functions.
- Use parameters and arguments.
- Set default parameter values.
- Return values from functions.
- Return multiple values from a function.
- Import a Python module.
- Understand the `if __name__ == '__main__'` statement.
- Organize code using functions.

## 3. Environment

- Operating System: Ubuntu 24.04
- Python Version: 3.12.3
- Repository: Python-Automation

Check Python version:

```bash
python3 --version
```

## 4. Task 1 – Creating a Simple Function

A function is a reusable block of code that performs a specific task.

### Example

```python
def greet(name):
    print(f"Hello, {name}!")

def main():
    greet("Alice")
    greet("Bob")

if __name__ == '__main__':
    main()
```

### Output

```text
Hello, Alice!
Hello, Bob!
```

### Explanation

- `def` is used to define a function.
- `greet` is the function name.
- `name` is a parameter.
- `greet("Alice")` calls the function with an argument.
- `main()` controls the program execution.
- The `if __name__ == '__main__':` guard runs `main()` when the file is executed directly.

## 5. Task 2 – Function Parameters and Return Values

Functions can accept parameters and return results.

### Final functions.py Code

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

def min_max(numbers):
    return min(numbers), max(numbers)

def main():
    greeting1 = greet("Alice")
    greeting2 = greet("Bob")
    print(greeting1)
    print(greeting2)
    print(greet("Carol", "Hi"))

    low, high = min_max([3, 9, 1, 7])
    print(low, high)

if __name__ == '__main__':
    main()
```

### Output

```text
Hello, Alice!
Hello, Bob!
Hi, Carol!
1 9
```

### Explanation

- `name` is a required parameter.
- `greeting="Hello"` is a default parameter.
- `return` sends a result back to the caller.
- `min_max()` returns two values: minimum and maximum.
- `low, high` receive the returned values.

## 6. Function Import Test

A Python file can be imported as a module into another Python program.

### Command

```bash
python3 -c 'import functions; print(functions.greet("X"))'
```

### Output

```text
Hello, X!
```

### Explanation

The import test confirms that the function can be reused from another Python command.

The `if __name__ == '__main__':` guard prevents `main()` from running automatically when the module is imported.

## 7. Task 3 – Function Modularity

Modularity means dividing a program into smaller functions.

### modularity.py Code

```python
def calculate_discount(price, discount):
    return price - (price * discount / 100)

final_price = calculate_discount(1000, 10)
print(final_price)
```

### Output

```text
900.0
```

### Explanation

- `calculate_discount()` performs the discount calculation.
- `price` represents the original price.
- `discount` represents the discount percentage.
- The function returns the final price.

## 8. Python Syntax Validation

### Command

```bash
python3 -m py_compile functions.py modularity.py
```

### Result

```text
Syntax validation passed.
```

This confirms that both Python files passed syntax compilation.

## 9. Project Structure

```text
Lab-08-Creating-and-Using-Functions/
│
├── .gitignore
├── README.md
├── functions.py
├── modularity.py
│
└── evidence/
    └── task-outputs.txt
```

## 10. Important Concepts Learned

| Concept | Description |
|---|---|
| Function | Reusable block of code |
| `def` | Defines a function |
| Parameter | Variable accepted by a function |
| Argument | Actual value passed to a function |
| Default parameter | Parameter with a predefined value |
| `return` | Sends a result back |
| Module | Python file that can be imported |
| Modularity | Dividing code into smaller parts |

## 11. Conclusion

In this lab, I learned how to create and call Python functions, use parameters and default arguments, return values, import modules, and organize code using modular functions.

The practical examples and syntax validation helped reinforce these Python fundamentals.

## 12. Evidence

The `evidence/task-outputs.txt` file contains the task outputs, function import test, and Python syntax validation result.
