from flask import Flask
import requests
import time
import smtplib
from email.message import EmailMessage
import hashlib
from urllib.request import urlopen
application = Flask(__name__)

@application.route("/")
# URL to monitor
url = 'http://127.0.0.1:8000/'
# Opens and reads the URL
response = urlopen(url).read()
# Store the contents of the webpage
currentHash = hashlib.sha224(response).hexdigest()

while True:

    try:

        response = urlopen(url).read()
        currentHash = hashlib.sha224(response).hexdigest()
        # waits 30 seconds
        time.sleep(30)
        response = urlopen(url).read()
        newHash = hashlib.sha224(response).hexdigest()
#If no change takes place nothing happens
        if newHash == currentHash:
            #print('Working as Expected')
            #smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
            #type(smtpObj)
            #conn = smtplib.SMTP('smtp-mail.outlook.com', 587)
            #conn
            #conn.ehlo()
            #conn.starttls()
            #conn.login('email login', 'email password')
            #conn.sendmail('aaron.houtsma@cslplasma.com', 'aaron.houtsma@cslplasma.com', message)
            #conn.quit 
            continue

        else:
#If a change has occured an email will be sent
            print('A status change has occured')
            #message = """\
#Subject: Donor 360 Application Login Page Status Changed


#Please check https://donor360.cslplasma.com/home and investigate as needed."""
            #smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
            #type(smtpObj)
            #conn = smtplib.SMTP('smtp-mail.outlook.com', 587)
            #conn
            #conn.ehlo()
            #conn.starttls()
            #conn.login('email login', 'email password')
            #conn.sendmail('aaron.houtsma@cslplasma.com', 'aaron.houtsma@cslplasma.com', message)
            #conn.quit            
            response = urlopen(url).read()
            currentHash = hashlib.sha224(response).hexdigest()
            time.sleep(30)
            continue
#If there is an exception it will be emailed
    except Exception as e:
        print(e)
        #message = """\
#Subject: Donor 360 Application Login not available


#Please investigate and contact HSS as needed."""
        #smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
        #type(smtpObj)
        #conn = smtplib.SMTP('smtp-mail.outlook.com', 587)
        #conn
        #conn.ehlo()
        #conn.starttls()
        #conn.login('email login', 'email password')
        #conn.sendmail('aaron.houtsma@cslplasma.com', 'aaron.houtsma@cslplasma.com', message)
        #conn.quit
        time.sleep(30)


if __name__ == "__main__":
    application.run()
