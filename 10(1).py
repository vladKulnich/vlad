x='sentences.txt'
f=open(x,"r") 
words=0
crapka=0
okluk=0
pitanna=0
for line in f:
    print (line)
    words += len(line.split())
    s=list(line)
    for e in s:
        if e==".":
            crapka= crapka+1
        elif e=="!":
            okluk=okluk+1
        elif e=="?":
            pitanna=pitanna+1
print("cлів ",words)
print("розповідних  ",crapka)
print("окличні ",okluk)
print("питальні  ",pitanna)



