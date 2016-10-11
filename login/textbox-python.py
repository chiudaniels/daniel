from flask import Flask, render_template, request, session, redirect, url_for
import csv, hashlib, os
from utils import action

app = Flask(__name__)
app.secret_key = "hehexd"


@app.route("/")
@app.route("/login/")
def template():
    if 'user' in session:
        return render_template('worked.html')
    else:
        return render_template('textbox.html', message='')

@app.route("/authenticate/", methods=['POST'])
def auth():
     if request.form['submit'] == 'register':
         if action.register(request.form['username'],request.form['password']):
             return render_template('textbox.html', message = 'username and password succesfully registered')
         else:
             return render_template('textbox.html', message = 'username already exsists')
     elif request.form['submit'] == 'login':
         #session.pop('user')
         if action.authenticate(request.form['username'],request.form['password']):
             session["user"] = request.form['username']
             return render_template('worked.html')
         else:
             return render_template('textbox.html', message='invalid username or password')

@app.route("/logout/", methods = ['POST'])
def logout():
    session.pop('user')
    return redirect (url_for('template'))
    

if __name__ == '__main__':
    app.debug = True
    app.run()
