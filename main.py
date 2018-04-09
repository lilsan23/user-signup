from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__) 

app.config['DEBUG'] = True

@app.route("/")
def create_signup():
    return render_template('signup.html')

@app.route("/", methods=['POST'])
def hello():
    user_id = request.Form('username')


    if len(user_id) <3 or len(user_id)==0:
        userid_error = "Username does not meet requirements. Try again"
        user_id=""
        return userid_error
    else:
    return render_template('hello.html', username=user_id)

    if 

app.run()