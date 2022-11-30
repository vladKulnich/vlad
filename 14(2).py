from bs4 import BeautifulSoup
import requests 
import os 
import shutil 
s=[]
s1=[]
r=requests.get('https://repetitor.org.ua/shtuchni-suputniki-zemli-2') 
if r.status_code==200: 
    wbs=BeautifulSoup(r.text,'html.parser')     
    for link in wbs.find_all("a"):        
        if 'href' in link.attrs:
            if 'png' in link.attrs['href']:
                print(link.attrs['href'])
                s.append(link.attrs['href'])
for i in s:
    s1.append(requests.get(i))
n=['G:\\код pyton\\new_image.gif','G:\\код pyton\\new_image2.gif','G:\\код pyton\\new_image3.gif']
a=0
os.mkdir("G:\код pyton\photo")
for i in s1 : 
    with open(n[a], 'wb') as f: 
        f.write(i.content)
    shutil.move(n[a], "G:\код pyton\photo")
    a+=1
    
    













