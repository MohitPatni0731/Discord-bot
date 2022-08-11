"""
To use this script you need two things - One is your Google app password which is different from your account password and the webhook url of a Discord channel in which you want bot to send message.

1. How to get app password of Google account
- Go to https://myaccount.google.com/ and then click on Security tab then on app passwords.
- Now in the Select app menu select the other option and then write python and then click on generate password.
- Now the password is appearing on your screen. Now, use that password in the script.

2. How to get webhooks url from Discord channel
- Go to your desired channel in which you want to message and ensure that you are the admin of that server.
- Now click on Edit channel, then click on Integrations
- Now click on Webhooks and then on create webhooks url. Now, use that url in the script.
"""


import requests
from dhooks import Webhook
import bs4
import time
import json
import os
from email.message import EmailMessage
import ssl
import smtplib


def get_current_price():
    """Extracting the value of British Pound in Indian Rupees"""
    currency = "convert 1 GBP to INR"
    url = f"https://google.com/search?q={currency}"
    fetch_value = requests.get(f"https://google.com/search?q={currency}")

    soup = bs4.BeautifulSoup(fetch_value.text, "html.parser")
    texts = soup.find("div", class_="BNeawe iBp4i AP7Wnd").text
    texts_split = texts.split(" ")
    get_current_price.current_price = float(texts_split[0])
    
    
def discord_bot():
    """Using webhook we send the message in the Discord server"""
    hook = Webhook("Paste the webhook link url of the Discord channel -- ")

    # Defining the upper and lower limit to get the alert when it will be triggered
    upper_limit = float(input("Enter the upper limit you want to set -- "))
    lower_limit = float(input("Enter the lowwer limit you wawnt to set -- "))
    
    if get_current_price.current_price >= upper_limit:
        hook.send(f"ALERT HIGH PRICE: Current price of 1 British Pound is = {str(get_current_price.current_price)} Indian Rupees")
        upper_limit += 0.50

    elif get_current_price.current_price <= lower_limit:
        hook.send(f"ALERT LOW PRICE: Current price of 1 British Pound is = {str(get_current_price.current_price)} Indian Rupees")
        lower_limit -= 0.50

    else:
        hook.send(f"Current price of 1 British Pound is = {str(get_current_price.current_price)} Indian Rupees")
            
            
def send_email():
    """Sending automated email"""
    sender = str(input('Enter your email -- ')
    password = input('Enter your password -- ')
    reciever = str(input('Enter email address you want to send mail to -- '))

    subject = 'AUTOMATED Pound rate email'
    body = f'Current price of 1 British Pound is = {str(get_current_price.current_price)} Indian Rupees'

    em = EmailMessage()
    em['From'] = sender
    em['To'] = reciever
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    port_number = 465
    with smtplib.SMTP_SSL('smtp.gmail.com', port_number, context=context) as smtp:   
        smtp.login(sender, password)
        smtp.sendmail(sender, reciever, em.as_string())

while 1:                 
    getting_current_price()
    discord_bot()
    send_email()    
    time.sleep(45*60)
