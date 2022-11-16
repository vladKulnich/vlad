def byk():
    global line
    hol=0
    A=("e","y","u","i","o","a")
    line=line.lower()
    s=list(line)
    for i in s:
        if i in A:
            hol +=1
    return(hol)        
f=open('sentences.txt',"r")
a=0
for line in f:
    a+=byk()
print("всього голосних: " ,a)

    