from flask import Flask
import cgi

app = Flask(__name__) 

app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html')