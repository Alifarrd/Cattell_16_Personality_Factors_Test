
user=[10,10,10,10,11,10,10,10,10,10,10,10,10,10,10,10]
data=[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,15]
c=0
for i in range (0,16):
    dis=(user[i]-data[i])*(user[i]-data[i])
    c=c+dis
print(c)