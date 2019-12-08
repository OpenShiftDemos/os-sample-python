from flask import Flask
application = Flask(__name__)

@application.route("/hello")
def hello():
    return "GREENNss!"

if __name__ == "__main__":
    application.run()
