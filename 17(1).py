import pandas as pd 
s0=[]
s1=[]
s2=[]
s3=[]
s=[s0,s1,s2,s3]
ss=[]
n=0
fname='masiv.csv'
df=pd.read_csv(fname, sep=';',encoding='cp1251')
for e in s: 
    for i in df.loc[n]:
        e.append(i)
    n+=1
ss=[sum(s0),sum(s1),sum(s2),sum(s3)]
f=open('res.txt',"w") 
for i in ss:
    f.write(str(i)+'\n')
#print(df.info) 