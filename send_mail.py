import smtplib, ssl
import os
from email.mime.text import MIMEText


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "amamazikee@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "amamazikee@gmail.com"
    msg = MIMEText(message, "plain", "utf-8")
    msg["Subject"] = "Today's Python News"
    msg["From"] = username
    msg["To"] = receiver
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg.as_string())