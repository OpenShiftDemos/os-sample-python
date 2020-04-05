from flask import Flask
application = Flask(__name__)

@application.route("/hello")
def hello():
    return "Hello Aramco_NEWss!"

if __name__ == "__main__":
    application.run()
