from flask import Flask
application = Flask(__name__)

@application.route("/hello")
def hello():
    return "Hello JKEB-11 test 2 bugsss!"

if __name__ == "__main__":
    application.run()
