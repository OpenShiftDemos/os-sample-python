from flask import Flask
application = Flask(__name__)

@application.route("/hello")
def hello():
    return "SARAH_FINAL!"

if __name__ == "__main__":
    application.run()
