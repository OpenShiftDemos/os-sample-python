from flask import Flask
application = Flask(__name__)

@application.route("/hello")
def hello():
    return "Hello Aramco_NEW!"

if __name__ == "__main__":
    application.run()
