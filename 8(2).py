import numpy as np
import random
M=int(input("Введіть M "))
N=int(input("Введіть N "))
s=[]
a=np.zeros((M,N),dtype=np.int)
for i in range(M): 
    for j in range (N):         
        a[i][j]=random.randint(1,20) 
print(a)
for i in range(M):
    b=sum(a[i])
    s.append(b)
for i in range(M):
    if sum(a[i])==max(s):
        print("найбільша сума в рядку : ",a[i],"=",sum(a[i]))


