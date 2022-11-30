import requests 
from bs4 import BeautifulSoup
x='webpages.txt'
f=open(x,'r')
c=open('pythonwik.txt','w',encoding='utf-8')
v=open('сирник.txt','w',encoding='utf-8')
s=[c,v]
i=0
for line in f:
    print(line)
    r=requests.get(line)
    d=BeautifulSoup(r.text,'html.parser')
    for b in d.get_text():
        s[i].write(b)
        s[i].close
    i=i+1
f.close
        
        


