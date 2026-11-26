# Lab 01 – Installing and Setting Up Python

## 1. Lab Overview

This lab covers installing Python, checking the Python version, creating and running Python scripts, and setting up an isolated Python virtual environment.

**Environment:**
- Operating System: Ubuntu 24.04.5 LTS
- Python Version: 3.12.3
- Package Manager: APT
- Code Editor: GNU Nano 7.2
- Virtual Environment: Python `venv`
- Package Installer: pip 24.0

## 2. Task 1 – Install Python

Updated the Ubuntu package lists:

```bash
sudo apt-get update
```

Installed Python and the required packages:

```bash
sudo apt-get install -y python3 python3-venv python3-pip python-is-python3
```

**Purpose of the packages:**

- `python3`: Installs Python 3.
- `python3-venv`: Provides virtual environment support.
- `python3-pip`: Installs the Python package manager.
- `python-is-python3`: Makes the `python` command point to Python 3.

## 3. Task 2 – Verify Python and Run a Script

Checked the Python versions:

```bash
python3 --version
python --version
```

**Verified output:**

```text
Python 3.12.3
Python 3.12.3
```

Created the first Python script:

```bash
mkdir -p ~/lab
cd ~/lab
nano hello.py
```

Python code:

```python
print("Hello from Python")
```

Executed the script:

```bash
python3 hello.py
```

**Output:**

```text
Hello from Python
```

## 4. Task 3 – Nano Editor and Virtual Environment

This lab was completed in a terminal-only Ubuntu environment. GNU Nano was used as the text editor instead of graphical editors such as VS Code or PyCharm.

Checked the Nano version:

```bash
nano --version | head -n 1
```

**Verified output:**

```text
GNU nano, version 7.2
```

Created a Python virtual environment:

```bash
cd ~/lab
python3 -m venv ~/lab/venv
```

Activated the environment:

```bash
source ~/lab/venv/bin/activate
```

Checked pip:

```bash
pip --version
```

**Verified output:**

```text
pip 24.0 from /home/ubuntu/lab/venv/lib/python3.12/site-packages/pip (python 3.12)
```

Verified that the virtual environment was active:

```bash
~/lab/venv/bin/python -c 'import sys;print(sys.prefix!=sys.base_prefix)'
```

**Output:**

```text
True
```

Created the virtual environment test script:

```bash
nano ~/lab/hello_venv.py
```

Python code:

```python
import sys
print("Running in:", sys.prefix)
```

Executed the script:

```bash
python ~/lab/hello_venv.py
```

**Output:**

```text
Running in: /home/ubuntu/lab/venv
```

Deactivated the virtual environment:

```bash
deactivate
```

## 5. Project Files

```text
Lab-01-Installing-and-Setting-Up-Python/
├── .gitignore
├── README.md
├── hello.py
├── hello_venv.py
└── evidence/
    └── task-outputs.txt
```

## 6. Evidence

The `evidence/` directory contains the verified terminal outputs for:

- Ubuntu and Python version checks
- Nano editor version
- pip installation inside the virtual environment
- Virtual environment verification
- Successful execution of both Python scripts

The virtual environment is stored separately at `~/lab/venv` and is not included in the GitHub repository.

## 7. Key Learning Outcomes

After completing this lab, I learned how to:

1. Install Python and related packages on Ubuntu.
2. Verify Python versions using terminal commands.
3. Create and execute Python scripts.
4. Use Nano to edit Python files.
5. Create and activate a Python virtual environment.
6. Verify pip inside a virtual environment.
7. Run Python scripts inside an isolated environment.
8. Deactivate a virtual environment.

## 8. Conclusion

Successfully completed the Python installation and setup practical on Ubuntu 24.04.5 LTS. Verified Python 3.12.3, executed Python scripts, and created and tested an isolated virtual environment using `venv`.
