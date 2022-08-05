import requests
from dhooks import Webhook
import bs4
import time
import json
import os
from email.message import EmailMessage
import ssl
import smtplib


def getting_current_price():
    """Extracting the value of British Pound in Indian Rupees"""
    currency = "convert 1 GBP to INR"
    url = f"https://google.com/search?q={currency}"
    request_result = requests.get(f"https://google.com/search?q={currency}")

    soup = bs4.BeautifulSoup(request_result.text, "html.parser")
    texts = soup.find("div", class_="BNeawe iBp4i AP7Wnd").text
    texts_split = texts.split(" ")
    getting_current_price.current_price = float(texts_split[0])
    
    
def discord_bot():
    """Using webhook we send the message in the Discord server"""
    hook = Webhook("Paste the webhook link url of the Discord channel -- ")

    # Defining the upper and lower limit to get the alert when it will be triggered
    upper_limit = 96.50
    lower_limit = 96.40
    
    if getting_current_price.current_price >= upper_limit:
        hook.send(f"ALERT HIGH PRICE: Current price of 1 British Pound is = {str(getting_current_price.current_price)} Indian Rupees")
        upper_limit += 0.50

    elif getting_current_price.current_price <= lower_limit:
        hook.send(f"ALERT LOW PRICE: Current price of 1 British Pound is = {str(getting_current_price.current_price)} Indian Rupees")
        lower_limit -= 0.50

    else:
        hook.send(f"Current price of 1 British Pound is = {str(getting_current_price.current_price)} Indian Rupees")
            
            
def send_email():
    """Sending automated email"""
    sender = str(input('Enter your email -- ')
    password = input('Enter your password -- ')
    reciever = str(input('Enter email address you want to send mail to -- '))

    subject = 'AUTOMATED Pound rate email'
    body = f'Current price of 1 British Pound is = {str(getting_current_price.current_price)} Indian Rupees'

    em = EmailMessage()
    em['From'] = sender
    em['To'] = reciever
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:   
        smtp.login(sender, password)
        smtp.sendmail(sender, reciever, em.as_string())
  
getting_current_price()
discord_bot()
send_email()
    
time.sleep(1000)
