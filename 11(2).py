import json
with open('дороги22.json', 'r') as jsonfile: 
    a=json.load(jsonfile)
print(a)
s=[]
f=""
for i in a:
    s.append(a[i])
d=sum(s)/len(s)
d=round(d,1)
for i in a:
    if a[i]<d:
        f=f+i+","
f=f[:-1]
print("середня довжина всіх доріг " +str(d))
print("назви доріг, чия довжина менша від середньої довжини всіх доріг: " + f)






   
    