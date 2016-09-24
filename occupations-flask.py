from flask import Flask, render_template

#################################################
#code for csv file
a = open('occupations.csv')
a.readline()
name = []
perc = []
for line in a:
  b = line.rfind(",")
  name.append(line[0:b])
  perc.append((line.replace("\n",""))[b+1:])
dictionary=dict (zip(name,perc))
##################################################
#print name
app= Flask(__name__)

@app.route("/occupations")
def template():
    return render_template('occupations-html.html',occupation=dictionary)
    
if __name__ == '__main__':
    app.debug= True
    app.run()
