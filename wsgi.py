from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "C2C24 Demo Python App"

if __name__ == "__main__":
    application.run()
