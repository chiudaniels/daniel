from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def template():
    return render_template('textbox.html')

@app.route("/authenticate/", methods=['POST'])
def worked():
    if request.form['username'] == 'daniel' and request.form['password'] == 'chiu':
        return "hello"
    else:
        return "didn't work"

@app.route("/failed/")
def didntWork():
    return render_template('failure.html')

    
if __name__ == '__main__':
    app.debug = True
    app.run()
