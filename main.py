from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__) 

app.config['DEBUG'] = True

@app.route("/")
def create_signup():
    return render_template('signup.html')

@app.route("/", methods=['POST'])
def hello():
    user_id = request.form['username']
    pass_word = request.form['password']
    ver_password = request.form['verify_password']
    email = request.form['email']

    userid_error = ""
    password_error = ""
    ver_password_error = ""
    email_error = ""
    email2_error = ""

    if len(user_id)<3 or user_id =="" or (" " in user_id):
        userid_error = "Username does not meet requirements. Try again."

    if len(pass_word) <3 or len(pass_word) >8:
        password_error = "Password does not meet requirements. Try again."
        pass_word=""
    
    if not ver_password == pass_word: 
        ver_password_error = "Password does not match."
        ver_password="" 
            
    if email !="":
        not ('@' in email or '.' in email or len(email) >3 or len(email) <20)
        email_error = "Email should contain '@' and '.'."
               # email2_error = "Email must be between 3 and 20 characters."
  
    if not userid_error and not password_error and not email_error and not email2_error:
        return render_template('hello.html', username=user_id)

    else:
        return render_template('signup.html', userid_error=userid_error, 
            password_error=password_error, 
            ver_password_error=ver_password_error,
            email_error=email_error, 
           # email2_error=email2_error,
            user_id=user_id,
            password=pass_word,
            verify_password=ver_password,
            email=email)
      

app.run()