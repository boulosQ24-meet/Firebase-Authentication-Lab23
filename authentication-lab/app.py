from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


Config = {
  "apiKey": "AIzaSyCvXSClwtv85sbJgxNJq1Gt9yXPWIdSmbY",
  "authDomain": "meettesty2boulos.firebaseapp.com",
  "projectId": "meettesty2boulos",
  "storageBucket": "meettesty2boulos.appspot.com",
  "messagingSenderId": "997430567535",
  "appId": "1:997430567535:web:8d762221f7e033c7d8e39a",
  "measurementId": "G-MH1LKJHK9P"
   "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()




@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.methods == "POST":
        try:
            email = request.form['email']
            password = request.form['password']
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)