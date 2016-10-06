from flask import Flask, render_template, request
import csv, hashlib

logindata='data/loginData'

def getUsers():
    f = open( logindata, 'r')
    data = f.read().strip()
    f.close()
    data = data.split('\n')
    users = {}
    if data[0] == '':
        return users
    for line in data:
        line = line.split(',')
        users[line[0]] = line[1]
    return users

def register(username, password):
    data=getUsers()
    
    if username in data:
        return render_template('textbox.html', message = 'username already exsists')
    else:
        password = hashlib.sha512(password).hexdigest()
        f= open(logindata,'a')
        f.write( username + ',' + password + '\n' )
        f.close()
        return render_template('textbox.html', message = 'username and password succesfully registered')

def authenticate(username,password):
    data=getUsers()
    password = hashlib.sha512(password).hexdigest()
    if username in data and password == daat[username]:
        return render_template('worked.html')
    else:
        return render_template('textbox.html', message='invalid username or password') 

def worked():
    if request.form['submit'] == 'register':
        register()
    elif request.form['submit'] == 'login':
        authenticate()
