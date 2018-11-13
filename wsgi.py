
import os,sys
from stat import *
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/alive")
def alive():
    return "Alive"

@application.route("/ready")
def ready():
    mode = os.stat("/").st_mode
    msg = "Ready: %s" % mode
    return msg

if __name__ == "__main__":
    application.run()
