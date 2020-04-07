from flask import Flask
application = Flask(__name__)

@application.route("/hello")
def hello():
    return "Hello Ara!"

if __name__ == "__main__":
    application.run()
from PIL import Image
myImage = Image.open("https://m.aawsat.com/sites/default/files/styles/article_img_top/public/2019/10/21/aramco.jpg?itok=2KgYvTDl");
myImage.show();
