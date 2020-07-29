from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    print ("updated messages")
    return "Hello World!"

if __name__ == "__main__":
    application.run()
