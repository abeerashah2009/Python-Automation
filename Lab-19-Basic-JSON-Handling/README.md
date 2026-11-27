# Lab 19 – Basic JSON Handling

## 1. Objective

The objective of this lab is to retrieve JSON data from an API, convert it into a Python dictionary, extract specific information, and save the extracted data into a JSON file.

## 2. Environment

- Operating System: Ubuntu 24.04 LTS
- Python Version: Python 3.12.3
- Library: Requests 2.32.3
- API: JSONPlaceholder
- API Endpoint: https://jsonplaceholder.typicode.com/posts/1

## 3. Concepts Learned

### JSON (JavaScript Object Notation)
JSON is a lightweight data format used to store and exchange information between applications.

### HTTP GET Request
A GET request retrieves information from a server.

### Status Code 200
HTTP status code 200 indicates that the request was successful.

### raise_for_status()
This method raises an exception if the HTTP response indicates an unsuccessful request.

### response.json()
This method converts a JSON API response into Python data, such as a dictionary.

### Python Dictionary
A dictionary stores information as key-value pairs.

Example:
- title: Post title
- body: Post content

### json.dump()
This method writes Python data into a JSON file.

### indent=4
This option formats JSON output with four spaces for readability.

### json.load()
This method reads and parses JSON data from a file.

## 4. Tasks Completed

1. Sent an HTTP GET request to the JSONPlaceholder API.
2. Checked the response using raise_for_status().
3. Retrieved JSON response data.
4. Converted the response into a Python dictionary.
5. Extracted the title and body fields.
6. Saved the extracted information into post_info.json.
7. Validated the saved JSON file.

## 5. Project Files

- fetch_json.py – Python script for retrieving and processing API data.
- post_info.json – Extracted JSON data.
- evidence/task-outputs.txt – Lab execution evidence.
- README.md – Lab notes and documentation.

## 6. Verification Results

- API request: Successful (HTTP 200)
- JSON parsing: Successful
- Dictionary conversion: Successful
- Data extraction: Successful
- JSON file creation: Successful
- JSON validation: Passed

## 7. Learning Outcome

I learned how to retrieve JSON data from an API, process it using Python dictionaries, extract required fields, and save the results into a formatted JSON file.
