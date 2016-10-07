from flask import Flask, render_template, request,session, redirect
import csv, hashlib, os
from utils import action

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def template():
    return render_template('textbox.html', message='')

@app.route("/authenticate/", methods=['POST'])
def login():
     if request.form['submit'] == 'register':
         if action.register(request.form['username'],request.form['password']):
             return render_template('textbox.html', message = 'username and password succesfully registered')
         else:
             return render_template('textbox.html', message = 'username already exsists')
     elif request.form['submit'] == 'login':
         if action.authenticate(request.form['username'],request.form['password']):
             session['user'] = request.form['username']
             return redirect(url_for('/session/'))
         else:
             return render_template('textbox.html', message='invalid username or password')

@app.route("/session/")
def session():
    if session['user'] == request.form['user']:
        return render_template('worked.html')
    else:
        session.pop('user')
        session['user']= request.form['username']
    
if __name__ == '__main__':
    app.debug = True
    app.run()
