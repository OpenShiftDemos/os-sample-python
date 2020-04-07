from flask import Flask
application = Flask(__name__)

@application.route("/hello")
def hello():
    return "Hello WAWds!"

if __name__ == "__main__":
    application.run()
