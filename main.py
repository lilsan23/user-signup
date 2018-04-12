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
    
    if len(user_id)<3:
        userid_error = "Username does not meet requirements. Try again."
        user_id=""
        
    if not userid_error:
        return render_template('hello.html', username=user_id)
    
    else:
        return render_template('signup.html', userid_error=userid_error)

    # else:
    # return render_template('signup.html', userid_error=userid_error, password_error= password_error, 
    #     # ver_password_error=ver_password_error, 
    #     # verify_password=ver_password,
    #     username=user_id, 
    #     password=pass_word)
    
 
  

app.run()