#!/usr/bin/python
import os
from dotenv import load_dotenv

load_dotenv()

import smtplib

sender = 'feedmebdo@gmail.com'
receivers = ['feedmebdo@gmail.com']

def send_email(message):
    try:
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(os.getenv("GMAIL_USERNAME"), os.getenv("GMAIL_PASSWORD")) #login with mail_id and password
        session.sendmail(sender, receivers, message)    
        print("Successfully sent email")
    except Exception as e:
        print(e)
        print("Error: unable to send email")


send_email("Test 123")