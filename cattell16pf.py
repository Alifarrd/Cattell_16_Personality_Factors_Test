import csv
import math
import matplotlib.pyplot as plt
user=[]
data=[]
lab=[]
with open('input.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        user.append(row)
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        data.append(row)
x=data[0][1:]
lab.append(user[1][0])
data.pop(0)
user.pop(0)
l=len(data)

for j in range (0,l):
    c=0
    for i in range (1,17):
        b=int(data[j][i])
        a=int(user[0][i])
        dis=(a-b)*(a-b)
        c=c+dis
    d=math.sqrt(c)
    data[j].append(d)

data.sort(key=lambda x: x[(17)])
print ("Closest users are as follows:")
for i in range(0,10):
    print (i+1,data[i][0],' ','User Grade:',data[i][17])

yplot=[]
yfirst = data[0][1:17]
yuser=user[0][1:17]
y=[yuser,yfirst]
lab.append(data[0][0])
c=0
for i in y:
    name=lab[c]
    c+=1
    yplot.clear()
    for j in i:
        j=int(j)
        yplot.append(j)
    plt.plot(x, yplot, label=name)
plt.legend()
plt.show()