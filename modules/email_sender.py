import smtplib
from email.message import EmailMessage
import os

def send_email_with_attachment(sender_email, app_password, receiver_email, subject, body, attachment_path):

    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.set_content(body)

    # Attach the file
    with open(attachment_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(attachment_path)
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(msg)
            print(f"Report emailed to {receiver_email}")
    except Exception as e:
        print(f"Email sending failed: {e}")
