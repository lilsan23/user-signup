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
      if len(user_id)==0:
          userid_error = "Username does not meet requirements. Try again."
          user_id=""
          #return render_template('signup.html',userid_error=userid_error, username=user_id)
      if len(pass_word) <3 or len(pass_word) >8:
         password_error = "Password does not meet requirements. Try again."
         pass_word=""
      if (not ver_password) == pass_word: 
         ver_password_error = "Password does not match."
         ver_password=""    
        # return render_template('signup.html', password_error= password_error, ver_password_error=ver_password_error, password=pass_word, verify_password=ver_password)    
         return render_template('signup.html', userid_error=userid_error, password_error= password_error, 
                     ver_password_error=ver_password_error, 
                     verify_password=ver_password,
                     username=user_id, 
                     password=pass_word)
      #else:
        #return render_template('hello.html', username=user_id)

  

app.run()