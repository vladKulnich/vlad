import csv
a=[]
s=[]
n=0
q=""
with open('data.csv') as csvfile: 
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        d=(row[0].split(":"))
        a.append(d[1])
for i in range(0,len(a)):
            a[i]=int(a[i])
while n<len(a):
    if a[n]==min(a):
        s.append(n)
    n=n+1
for e in s:
    q=q+str(e+1)+","
q=q[:-1]
print("мінімальна продукція "+str(min(a))+" в такі дні квітня:" +q)
        


