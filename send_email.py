import smtplib, ssl
from secret import google_app_password as gap

HOST = "smtp.gmail.com"
PORT = 465

receiver = gap.USER
context = ssl.create_default_context()

message = """\
Subject: HI
hi,
greetings from python
"""

with smtplib.SMTP_SSL(HOST, PORT, context=context) as server:
    server.login(gap.USER, gap.PASSWORD)
    server.sendmail(gap.USER, receiver, message)


