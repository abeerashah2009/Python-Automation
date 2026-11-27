# Lab 27 – API Automation Example

## Objective

- Understand API automation using Python.
- Send HTTP POST requests using the `requests` library.
- Parse and inspect JSON responses from a web service.

## Environment

- OS: Ubuntu 24.04
- Python: 3.12
- Requests: 2.32.3
- API: https://httpbin.org/post

## Task 1 – Prepare Local Data

Created `api_automation_example.py` with a Python dictionary containing:

- Name: John Doe
- Email: john.doe@example.com
- Age: 30

Verified the initial script successfully.

## Task 2 – Send POST Request

Used the `requests.post()` method to send JSON data to the API endpoint.

- HTTP method: POST
- Endpoint: https://httpbin.org/post
- JSON payload: `user_data`
- Timeout: 10 seconds

**Result:** HTTP status code 200.

## Task 3 – Check Response and Parse JSON

Checked the HTTP response status code.

When the status code was 200:
- Displayed a success message.
- Parsed the response using `response.json()`.
- Displayed the complete response data.
- Extracted the submitted JSON using `response_data['json']`.

**Result:** The API successfully returned the submitted name, email, and age.

## Curl Comparison

Used curl to send another POST request to the same endpoint.

The response confirmed the POST method and API endpoint.

## SSL Certificate Configuration

The lab environment uses a local HTTPS proxy. Configured Python requests to use the Ubuntu system certificate bundle:

`REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt`

SSL certificate verification remained enabled.

## Files

- `api_automation_example.py` – API automation script.
- `evidence/task-outputs.txt` – Lab execution evidence.
- `.gitignore` – Excludes virtual environment and Python cache files.

## Learning Outcomes

- Created a Python dictionary for JSON data.
- Installed and used the requests library.
- Sent HTTP POST requests.
- Checked HTTP response status codes.
- Parsed JSON responses.
- Extracted specific data from an API response.
- Compared API requests using Python and curl.

## Conclusion

Successfully completed the API automation example. The POST request returned HTTP 200, and the JSON response was parsed to retrieve the submitted data.
