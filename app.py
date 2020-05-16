from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print('hello world')
    return "Hello World!"
