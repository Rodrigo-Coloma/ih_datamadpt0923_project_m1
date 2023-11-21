import smtplib
from dotenv import dotenv_values
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def email(recipient_email):
    if recipient_email:
        sender_email = "wilfredtours@gmail.com"
        sender_password = dotenv_values('./.env')['PWD_GMAIL']
        subject = "Checkout yor personalized tour!!"
        body = "Dear traveler,\n\nPlease find attached a map with you customized route for visiting your chosen madrid monuments. Note that we have included some other interest places and restaurants near the stops.\n\nHave a nice day!\n"
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        file_path = f"./templates/route_map.html"  
        attachment = open(file_path, "rb")
        file_mime = MIMEApplication(attachment.read(), _subtype="html")  
        attachment.close()
        file_mime.add_header('Content-Disposition', 'attachment', filename="Your_personalized_route.html")
        message.attach(file_mime)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.quit()
    


 