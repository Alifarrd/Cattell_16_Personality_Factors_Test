from cmath import sqrt
import csv
import math
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
