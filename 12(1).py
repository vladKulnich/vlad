def pr(x):
    s=list(x)
    for i in s:
        print(i)
def spad(x):
    s1=[]
    s=list(x)
    for i in range(0,len(s)):
            s[i]=int(s[i])
    s.sort()
    for i in range(1,len(s)+1):
        s1.append(s[-i])
    for i in s1:
        print(i)
a=input("Введіть число  ")
pr(a)
print("спадає")
spad(a)