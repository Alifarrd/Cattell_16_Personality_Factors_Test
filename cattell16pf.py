from cmath import sqrt
import csv
import math
user=[10,10,10,10,11,10,10,10,10,10,10,10,10,10,10,10]
re=[]
c=0
data=[]
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        data.append(row)
for j in range (1,51):
    for i in range (0,16):
        b=int(data[j][i])
        dis=(user[i]-b)*(user[i]-b)
        c=c+dis
        c=math.sqrt(c)
    re.append(c)
re.sort()

for k in range(0,10):
    print(re[k])
