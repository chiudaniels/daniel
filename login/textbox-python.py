from flask import Flask, render_template, request
import csv, hashlib

app = Flask(__name__)

datalist={}

def opendata():
    with open('loginData.csv', 'rb') as csvfile:
        data=csv.DictReader(csvfile)
        datalist= dict(data)

@app.route("/")
def template():
    return render_template('textbox.html')

@app.route("/authenticate/", methods=['POST'])
def worked():
    opendata()
    if request.form['submit'] == 'register':
        if datalist.has_key(request.form['username']):
            return render_template('textbox.html', message = 'username already exsists')
        else:
            with open('loginData.csv','wb') as csvfile:
                fieldname=['username','password']
                cred=csv.DictWriter(csvfile, fieldnames=fieldname)
                password= hashlib.sha512(request.form['password'])
                cred.writeheader()
                cred.writerow({'username':request.form['username'], 'password':password.hexdigest()})
                return render_template('textbox.html', message = 'username and password succesfully registered')
    elif request.form['submit'] == 'login':
        if datalist.has_key(request.form['username']):
            if datalist.get(request.form['username']) == hashlib.sha512(request.form['password']).hexdigest():
                return render_template('worked.html')
            else:
                return render_template('textbox.html', message='invalid username or password') 

if __name__ == '__main__':
    app.debug = True
    opendata()
    app.run()
