from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


Config = {
    'apiKey': "AIzaSyCvXSClwtv85sbJgxNJq1Gt9yXPWIdSmbY",
    'authDomain': "meettesty2boulos.firebaseapp.com",
    'projectId': "meettesty2boulos",
    'storageBucket': "meettesty2boulos.appspot.com",
    'messagingSenderId': "997430567535",
    'appId': "1:997430567535:web:8d762221f7e033c7d8e39a",
    'measurementId': "G-MH1LKJHK9P",
    "databaseURL": "https://meettesty2boulos-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()




@app.route('/', methods=['GET', 'POST'])
def signin():
    error=''
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
        except:
            error = "error habibi"
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error=''
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
        except:
            error = "error habibi"
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)