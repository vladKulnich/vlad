import pandas as pd 
import json
from datetime import datetime
s=[]
sn=[]
sd=[]
sdata=[]
with open('name.json', 'r') as jsonfile:
    a=json.load(jsonfile)

for i in a:
    s=a[i].split(" ")
    sn.append(s[0])
    sd.append(s[1])

for i in sd:
    sdata.append(str(datetime.strptime(i,"%d.%m.%Y")))
q=pd.Series(sdata,sn)
print(q)
f=dict(q)
with open('dtm.json', 'w') as file:
    json.dump(f,file)
