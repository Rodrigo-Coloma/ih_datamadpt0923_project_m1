import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import dotenv_values

def email(receiver, folder):
    mail = smtplib.SMTP()
    sender = ('rjcolgut@gmail.com')
    receivers = [receiver.strip()]
    mail.sendmail()


 