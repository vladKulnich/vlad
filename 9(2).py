import math 
A={-5,3,0,7}
s=list(A)
print(s)
s1=[]
B=set()
for e in s:
    n=0
    while not n==len(s)-1:
        w=int(math.fabs(s[n]-e))
        s1.append(w)
        B.add(w)
        n=n+1
B.discard(0) 
print(s1)
print(B)
