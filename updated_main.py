import requests
from dhooks import Webhook
import bs4
import time
import json
import os
from email.message import EmailMessage
import ssl
import smtplib

# Running a for loop to get the latest price of the GBP
While True:

    def Getting_current_price():
        """Extracting the value of British Pound in Indian Rupees"""
        currency = "convert 1 GBP to INR"
        url = f"https://google.com/search?q={currency}"
        request_result = requests.get(f"https://google.com/search?q={currency}")

        soup = bs4.BeautifulSoup(request_result.text, "html.parser")
        temp = soup.find("div", class_="BNeawe iBp4i AP7Wnd").text
        temps = temp.split(" ")
        current_price = float(temps[0])
    Getting_current_price()
    
    
    def Discord_bot():
        """Using webhook we send the message in the Discord server"""
        hook = Webhook(
            "https://discord.com/api/webhooks/1003993992360366080/1cS8w3N2GHzW-2aAwLYZ9tpfcHHhRBiASgTIafnfJ1Q--NbC1Exat7lVVzr4mgvH3l5f"
        )

        # Defining the upper and lower limit to get the alert when it will be triggered
        upper_limit = 96.50
        lower_limit = 96.40

        if current_price >= upper_limit:
            high_price_alert = (
                "ALERT HIGH PRICE: Current price of 1 British Pound is = "
                + str(current_price)
                + " Indian Rupees"
            )
            hook.send(high_price_alert)
            upper_limit += 0.50

        elif current_price <= lower_limit:
            low_price_alert = (
                "ALERT LOW PRICE: Current price of 1 British Pound is = "
                + str(current_price)
                + " Indian Rupees"
            )
            hook.send(low_price_alert)
            lower_limit -= 0.50

        else:
            current_price_alert = (
                "Current price of 1 British Pound is = "
                + str(current_price)
                + " Indian Rupees"
            )
            hook.send(current_price_alert)
    Discord_bot()
            
            
    def send_email():
        """#Sneding automated email"""
        sender = 'mohitpatni0731@gmail.com'
        password = 'ckyryrdajffgmnde'
        reciever = 'mohitpatni786@gmail.com'

        subject = 'AUTOMATED Pound rate email'
        body = 'Current price of 1 British Pound is = '+str(current_price)+' Indian Rupees'

        em = EmailMessage()
        em['From'] = sender
        em['To'] = reciever
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:   
            smtp.login(sender, password)
            smtp.sendmail(sender, reciever, em.as_string())
    send_email()
    
    time.sleep(1000)
