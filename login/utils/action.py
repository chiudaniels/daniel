from flask import Flask, render_template, request
import csv, hashlib

logindata='data/loginData.csv'

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
        return False
    else:
        password = hashlib.sha512(password).hexdigest()
        f= open(logindata,'a')
        f.write( username + ',' + password + '\n' )
        f.close()
        return True

def authenticate(username,password):
    data=getUsers()
    password = hashlib.sha512(password).hexdigest()
    if username in data and password == data[username]:
        return True
    else:
        return False 

def worked():
    if request.form['submit'] == 'register':
        return register(request.form['username'],request.form['password'])
    elif request.form['submit'] == 'login':
        return authenticate(request.form['username'],request.form['password'])
