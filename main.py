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
    email = request.form['email']

    if len(user_id)<3 or user_id =="" or (" " in user_id):
        userid_error = "Username does not meet requirements. Try again."
        user_id=""
        return render_template('signup.html', userid_error=userid_error)
        
    if (not '@' in email) or (not '.' in email):
        email_error = "Email should contain '@' and '.'."
        email=""
        return render_template('signup.html', email_error=email_error)
        
    if len(email) <3 or len(email) >20:
        email2_error = "Email must be between 3 and 20 characters."
        email="" 
        return render_template('signup.html', email2_error=email2_error)

    else:
        return render_template('hello.html', username=user_id,email=email)

    # else:
    # return render_template('signup.html', userid_error=userid_error, password_error= password_error, 
    #     # ver_password_error=ver_password_error, 
    #     # verify_password=ver_password,
    #     username=user_id, 
    #     password=pass_word)
    
 
app.run()