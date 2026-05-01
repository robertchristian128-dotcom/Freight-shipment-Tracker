import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_ADDRESS, APP_PASSWORD

EMAIL = "robertchristian128@gmail.com"
APP_PASSWORD = "ylzxgrkvflshophl"


def send_email(to, subject, body):

    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = "x89logistics@outlook.com", "robertchristian128@gmail.com"
    msg["Subject"] = "In Transit"
    msg.attach(MIMEText(body, "plain"))
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, APP_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to, msg.as_string())
        print(f"Email sent to {to}")