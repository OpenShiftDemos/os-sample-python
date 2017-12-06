from flask import Flask
import time
from datetime import date
application = Flask(__name__)

@application.route("/")
def hello():
    today = date.today()
    #april1 = date(2018, 4, 1)
    countdownstring = "C2C24 Demo Python App "
    countdownstring += "Days to April 1"
    #if april1 > today:
        #time_to_april1 = abs(april1 - today)
        #days_to_april1 = time_to_april1.days
        #countdownstring += " Days to April 1: "
        #countdownstring.append(days_to_april1)
    return countdownstring

if __name__ == "__main__":
    application.run()
