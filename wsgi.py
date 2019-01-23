from flask import Flask, render_template, request, redirect, session, flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_LETTER_REGEX = re.compile(r'.*[A-Z]+.*')
PASSWORD_NUM_REGEX = re.compile(r'.*[0-9]+.*')
app = Flask(__name__)
app.secret_key = 'registrationkey'

@app.route('/')
def index():
    if 'clear' in session:
        session.clear()
    return render_template('index.html')

@app.route('/register', methods=['POST','GET'])
def submit_info():
    if len(request.form['first_name']) < 1:
        flash("First name cannot be blank!", 'blank')
    if len(request.form['last_name']) < 1:
        flash("Last name cannot be blank!", 'blank')
    if len(request.form['password']) < 1:
        flash("Password cannot be blank!", 'blank')
    elif len(request.form['password']) < 8:
        flash("Password must be more than 8 characters long", 'error')
    elif not PASSWORD_LETTER_REGEX.match(request.form['password']):
        flash("Password must have 1 uppercase and 1 number", 'error')
    elif not PASSWORD_NUM_REGEX.match(request.form['password'], 'error'):
        flash("Password must have 1 uppercase and 1 number", 'error')
    elif request.form['password'] != request.form['confirm_password']:
        flash("Password must match confirmation!", 'error')
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", 'blank')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email must be valid", 'error')

    if '_flashes' in session.keys():
        return redirect('/')
    else:
        return redirect('/registered')

@app.route('/registered')
def complete():
    return render_template('registered.html')


# application = Flask(__name__)
#
# @application.route("/")
# def hello():
#     return "Hello World!"
#
#
# if __name__ == "__main__":
#     application.run()
