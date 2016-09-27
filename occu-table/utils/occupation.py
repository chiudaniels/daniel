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

def getRandom():
    return e
def getDict():
    return dictionary
