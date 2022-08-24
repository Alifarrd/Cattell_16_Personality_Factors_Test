from cmath import sqrt
import csv
import math
user=[]
re=[]
data=[]
with open('input.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        user.append(row)
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        data.append(row)
for j in range (1,51):
    c=0
    for i in range (0,16):
        b=int(data[j][i])
        a=int(user[1][i])
        dis=(a-b)*(a-b)
        c=c+dis
    d=math.sqrt(c)
    re.append(d)


re.sort()
#for k in range(0,10):
#    print(re[k])

print(re)
