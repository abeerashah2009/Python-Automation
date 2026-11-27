import smtplib
from email.mime.text import MIMEText

# SMTP server settings
smtp_server = '127.0.0.1'
smtp_port = 1025

# Sender and recipient email addresses
email_user = 'sender@example.com'
recipient_email = 'recipient@example.com'

# Email subject and body
subject = 'Test Email Subject'
body = 'This is a test email sent from a Python script.'

# Create the email message
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = email_user
msg['To'] = recipient_email

# Function to send the email
def send(port):
    try:
        server = smtplib.SMTP(smtp_server, port, timeout=5)
        server.sendmail(email_user, recipient_email, msg.as_string())
        server.quit()
        print(f"Email sent successfully via port {port}!")
    except Exception as e:
        print(f"An error occurred on port {port}: {e}")

# Send email using the configured SMTP port
send(smtp_port)
