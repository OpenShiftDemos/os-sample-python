from flask import Flask
application = Flask(__name__)

@application.route("/hello")
def hello():
    return "Hello dddddsd!"

if __name__ == "__main__":
    application.run()
