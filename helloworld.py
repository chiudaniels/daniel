from flask import Flask

app= Flask(__name__)

@app.route("/")
@app.route(“hehe”)
@app.route(“xd”)

def hello():
	return __name__+"hello world"
    
if __name__ == '__main__':
	app.run()