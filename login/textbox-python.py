from flask import Flask, render_template, request
import csv, hashlib
from utils import action

app = Flask(__name__)
                       
@app.route("/")
def template():
    return render_template('textbox.html')

@app.route("/authenticate/", methods=['POST'])
def login():
    action.worked()

if __name__ == '__main__':
    app.debug = True
    app.run()
