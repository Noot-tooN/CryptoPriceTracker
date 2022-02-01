# importing the requests library
import requests
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from send_mail import send_email

def getTrunkPrice():
    # api-endpoint
    addr = "https://api.pancakeswap.info/api/v2/tokens/0xdd325C38b12903B727D16961e61333f4871A70E0"
    
    # sending get request and saving the response as response object
    r = requests.get(url = addr)
    
    # extracting data in json format
    data = r.json()

    return data["data"]["price"]

currentPrice = 0

while True:
    data = getTrunkPrice()

    if float(data) >= 1:
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = "feedmebdo@gmail.com"
        message['To'] = "feedmebdo@gmail.com"
        message['Subject'] = 'TRUNK price'   #The subject line
        #The body and the attachments for the mail
        mailContent = f"""Current TRUNK price is: {data}"""
        message.attach(MIMEText(mailContent, 'plain'))

        send_email(message.as_string())
        # print(message)
    
    time.sleep(30)

