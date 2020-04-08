from flask import Flask
application = Flask(__name__)

@application.route("/hello")
def hello():
    return "Hello Test!"

if __name__ == "__main__":
    application.run()
