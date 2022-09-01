from cmath import sqrt
import csv
import math
from typing import Any
import matplotlib.pyplot as plt
import numpy as np
user=[]
data=[]
with open('input.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        user.append(row)
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        data.append(row)
x=data[0][1:]
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

for i in range(0,9):
    print (data[i][0])


y2=[]
y4=[]
y = data[1][1:17]
y3=user[0][1:17]

for i in y:
    i=int(i)
    y2.append(i)
for i in y3:
    i=int(i)
    y4.append(i)
plt.plot(x, y2, label="best mate")
plt.plot(x, y4, label="user")
plt.legend()
plt.show()
