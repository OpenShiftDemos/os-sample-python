from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"
@app.route('/upload_img',methods=['GET','POST'])
def upload_img():
    if request.method == 'POST':

       ###
       # why save img then read it TRY TO SOLVE
       ###
        #print(request.form)
        #img_str = request.form['pic']

        #img = request.form['pic_name']
        #convert_and_save(img_str, img_name)
        #
        print(request.files)
        print(request.form)
        img=request.files['pic']

        img.save(secure_filename(img.filename))
        #run_ocr(img.filename)
        #thread = threading.Thread(target=run_ocr(img.filename) )
        #thread.start()
        #global cur_filename
        #cur_filename = img.filename
        #print("post file name"+cur_filename)
        return "success hetr fgdfbd"+img.filename

if __name__ == "__main__":
    application.run()
