from flask import Flask, render_template, request
import csv, hashlib, action

app = Flask(__name__)
                       
@app.route("/")
def template():
    return render_template('textbox.html')

@app.route("/authenticate/", methods=['POST'])
def login():
    action.opendata()
    action.worked()

if __name__ == '__main__':
    app.debug = True
    action.opendata()
    app.run()
