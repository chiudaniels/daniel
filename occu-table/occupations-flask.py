from flask import Flask, render_template
import random
import occupation

app= Flask(__name__)

@app.route("/occupations")
def template():
    return render_template('occupations-html.html',occupation=occupation.getDict(), random_occ=occuapation.getRandom())
    
if __name__ == '__main__':
    app.debug= True
    app.run()
