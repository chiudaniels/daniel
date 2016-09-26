from flask import Flask, render_template
import random
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
del name[-1]
del perc[-1]
mess = []
d = 0
while d < len(name):
  c = float(perc[d]) * 10
  while c > 0:
    c = c - 1
    mess.append(name[d])
  d = d + 1
e = random.choice(mess)
##################################################
#print name
app= Flask(__name__)

@app.route("/occupations")
def template():
    return render_template('occupations-html.html',occupation=dictionary, random_occ=e)
    
if __name__ == '__main__':
    app.debug= True
    app.run()
