from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello Worldddd!"

if __name__ == "__main__":
    application.run()
