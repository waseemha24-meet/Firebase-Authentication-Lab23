from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
firebaseConfig = {
  "apiKey": "AIzaSyD5AJW0GE-HTxC_OZwBX5zR-bpzX1bhA7Q",
  "authDomain": "project-ca0e7.firebaseapp.com",
  "projectId": "project-ca0e7",
  "storageBucket": "project-ca0e7.appspot.com",
  "messagingSenderId": "169988340335",
  "appId": "1:169988340335:web:28da0e15395478d333eb9a",
  "measurementId": "G-1EDX44BGB8",
  "databaseURL": ""
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "Authetication faild"
    return render_template("add_tweet.html")

@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__': 
    app.run(debug=True)