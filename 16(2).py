import pylab 
import numpy as np 
def ff(a):
    return {c: a.count(c) for c in set(a)}
s1=[]
sx=[]
sy=[]
c=open('masuv.txt','r')
for line in c:
    line=line.replace("\n","")
    s=line.split(" ")
    for i in s:
        s1.append(i)
for i in range(0,len(s1)):
        s1[i]=int(s1[i])
z=ff(s1)
for i in set(s1):
    sx.append(i)
print(sx)
for i in sx:
    sy.append(z[i])
print(sy)
x=np.array(sx) 
y=np.array(sy) 
pylab.bar (x, y)  
pylab.show()