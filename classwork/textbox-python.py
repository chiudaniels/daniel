from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def template():
    return render_template('textbox.html')

@app.route("/authenticate/")
def worked():
    "worked" ==  request.form
    print worked
    
if __name__ == '__main__':
    app.debug = True
    app.run()
