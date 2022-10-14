q=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
a=int(input("Введіть кількість кутів многокутника:  "))
b=(input("Введіть першу  літеру  назви:  "))
s=[]
for e in q:
    if e==b:
        r=q.index(e)
        break
for i in range(a):
    s.append(q[r])
    r=r+1
    if r==len(q):
        r=0
        for j in range(a-len(s)):
            s.append(q[r])
            r=r+1
        break
print(s)
d=""
for i in range(0,len(s)):
    d=d+s[i]
print(d)

