from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__) 

app.config['DEBUG'] = True

@app.route("/", methods= ['Get','Post'])
def create_username():
    return render_template('signup.html')
app.run()