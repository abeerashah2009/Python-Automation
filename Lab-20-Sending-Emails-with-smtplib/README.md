# Lab 20 – Sending Emails with smtplib

## 1. Objective

The objective of this lab is to learn how to send emails using Python's built-in `smtplib` library.

In this lab, I created a Python script that connects to a local SMTP server, prepares an email message, sends it, and handles connection errors.

## 2. Environment

- Operating System: Ubuntu 24.04 LTS
- Python Version: 3.12.3
- SMTP Library: smtplib (Python standard library)
- Email Module: email.mime.text
- Mock SMTP Server: aiosmtpd 1.4.6
- SMTP Host: 127.0.0.1
- SMTP Port: 1025

## 3. Important Concepts

### What is SMTP?

SMTP stands for Simple Mail Transfer Protocol.

It is a communication protocol used to send emails between email systems.

### What is smtplib?

`smtplib` is a built-in Python library used to communicate with SMTP servers and send email messages.

### What is MIMEText?

`MIMEText` is used to create a text-based email message.

It allows us to define the email body and prepare message headers.

### What is an SMTP Server?

An SMTP server receives email messages from an email application and processes them for delivery.

In this lab, I used a local mock SMTP server to safely test email sending.

## 4. Tasks Performed

### Task 1 – SMTP Server Setup

- Created a Python virtual environment.
- Installed `aiosmtpd==1.4.6`.
- Started a local SMTP debugging server.
- Configured the server to listen on 127.0.0.1:1025.
- Verified that port 1025 was listening.

### Task 2 – Create an Email Script

Created `send_mail.py` using Python.

The script performs these operations:

1. Imports smtplib and MIMEText.
2. Defines the SMTP server address and port.
3. Defines sender and recipient email addresses.
4. Creates an email subject and body.
5. Adds Subject, From, and To headers.
6. Connects to the SMTP server.
7. Sends the email using sendmail().
8. Closes the connection using quit().

### Task 3 – Send and Verify Email

Executed:

`python send_mail.py`

Result:

`Email sent successfully via port 1025!`

Verified the received message in the SMTP server log.

The captured message contained:

- Subject: Test Email Subject
- From: sender@example.com
- To: recipient@example.com
- Body: This is a test email sent from a Python script.

### Task 4 – Error Handling

Used a try-except block to handle SMTP connection errors.

Tested an unavailable SMTP port (9999).

The connection timed out, and the script displayed an error message instead of crashing.

## 5. Security Considerations

- Never hardcode real email passwords inside Python scripts.
- Use environment variables or secure secret management.
- Real email providers may require an app password or OAuth authentication.
- Real SMTP connections should use appropriate TLS protection and authentication.
- This lab uses a local mock SMTP server without authentication or TLS because it is restricted to the loopback address 127.0.0.1.
- This local configuration must not be used as an external production email server.

## 6. Files Included

| File | Description |
|---|---|
| send_mail.py | Python email sending script |
| evidence/smtp-captured-message.txt | Captured email from the mock SMTP server |
| evidence/task-outputs.txt | Lab command outputs and verification results |
| .gitignore | Excludes temporary and Python cache files |

## 7. Verification Results

- Python syntax check: Passed
- SMTP server startup: Passed
- SMTP port listening check: Passed
- Email sending: Passed
- Email received and captured: Passed
- Error handling: Passed
- Git whitespace check: To be verified before commit

## 8. Learning Outcomes

After completing this lab, I learned:

- How to use Python smtplib.
- How to prepare an email using MIMEText.
- How SMTP connections work.
- How to send a text email using sendmail().
- How to handle connection errors using try-except.
- Why secure authentication and TLS are important when sending real emails.

**Lab 20 Status: Completed and verified locally.**
