from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:

        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin':
            return render_template('index.html')
        else:
            msg = 'Incorrect username or password!'
            print(msg)

    return render_template('login.html', msg=msg)

@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    msg = ''
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin':
            msg = 'Account already exists!'
        elif username == '' or password == '':
            msg = 'Please fill out the form!'
        else:
            msg = 'Account created! Please login.'
            time.sleep(3)
            return render_template('login.html', msg=msg)           

    return render_template('signup.html', msg=msg)

@app.route('/logout')
def logout_page():
    return render_template('logout.html')


