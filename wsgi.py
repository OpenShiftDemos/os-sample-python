from flask import Flask
application = Flask(__name__)

@application.route("/hello")
def hello():
    return "Hello AramsscoV2!"

if __name__ == "__main__":
    application.run()
