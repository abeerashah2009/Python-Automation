# Lab 18 - Using the Requests Module

## 1. Objective

The objective of this lab is to learn how to use Python's `requests` module to communicate with web APIs using HTTP GET requests.

This lab demonstrates how to:
- Install and import the Requests library.
- Send an HTTP GET request.
- Check the HTTP response status code.
- Convert a JSON response into Python data.
- Extract and display specific JSON fields.
- Handle connection errors and unsuccessful HTTP responses.

## 2. Environment

- Operating System: Ubuntu 24.04 LTS
- Python Version: 3.12.3
- Requests Version: 2.32.3
- Editor: Nano
- Virtual Environment: Python `venv`
- API: JSONPlaceholder

## 3. Important Concepts

### 3.1 Requests Module

The `requests` module is a Python library used to send HTTP requests and communicate with web servers and APIs.

Import it using:

```python
import requests
```

### 3.2 HTTP GET Request

A GET request retrieves information from a server.

Example:

```python
response = requests.get(URL, timeout=10)
```

The `timeout` parameter limits how long the program waits for a response.

### 3.3 Response Status Code

An HTTP status code tells us the result of a request.

- `200`: Request successful.
- `404`: Requested resource not found.
- Other unsuccessful status codes indicate that the request did not receive the expected response.

### 3.4 JSON Response

JSON (JavaScript Object Notation) is a common format for exchanging data between applications.

Convert a JSON response into Python data using:

```python
data = response.json()
```

Access individual fields using dictionary keys:

```python
data['title']
data['body']
```

### 3.5 Exception Handling

The `try` and `except` blocks handle request-related errors.

```python
try:
    response = requests.get(URL, timeout=10)
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
    sys.exit(1)
```

This prevents an unexpected connection error from stopping the program without a clear message.

### 3.6 Command-Line Arguments

The `sys` module allows a user to provide a URL when running the script.

```python
URL = sys.argv[1] if len(sys.argv) > 1 else "https://jsonplaceholder.typicode.com/posts/1"
```

If no URL is supplied, the program uses the default API endpoint.

## 4. Practical Tasks

### Task 1 - Install Requests

Create and activate a virtual environment, then install the required version:

```bash
python3 -m venv venv
source venv/bin/activate
pip install requests==2.32.3
```

Verify the installed version:

```bash
python -c 'import requests; print(requests.__version__)'
```

### Task 2 - Send a GET Request

The script sends a GET request to:

`https://jsonplaceholder.typicode.com/posts/1`

### Task 3 - Check the Response

The program checks whether the response status code is `200`.

If the status is not `200`, it displays an error message and exits with status code `1`.

### Task 4 - Parse JSON

The program extracts the `title` and `body` fields from the JSON response and prints them.

### Task 5 - Test Error Handling

A non-existent post URL is used to test the HTTP 404 response.

```bash
python post.py https://jsonplaceholder.typicode.com/posts/99999
echo $?
```

## 5. Verification Results

The following checks were successfully completed:

- Requests version verified: `2.32.3`
- Python syntax check passed.
- Successful API request returned HTTP 200.
- JSON title and body displayed correctly.
- Invalid resource returned HTTP 404.
- Error test returned exit code `1`.

The lab environment uses an HTTPS proxy. Ubuntu's trusted CA bundle was configured for Requests using:

```bash
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
```

SSL certificate verification remained enabled.

## 6. Project Files

- `post.py` - Python program that sends the GET request and processes the JSON response.
- `evidence/task-outputs.txt` - Actual terminal output showing installation verification, syntax check, successful request, and 404 test.
- `.gitignore` - Excludes Python cache files, virtual environments, and log files.

## 7. Learning Outcomes

After completing this lab, I learned how to:

1. Install and use an external Python library.
2. Send HTTP GET requests using Requests.
3. Understand HTTP response status codes.
4. Parse JSON data in Python.
5. Extract values from JSON responses.
6. Handle request exceptions.
7. Use command-line arguments to provide a custom API URL.
8. Verify successful and unsuccessful API requests.
