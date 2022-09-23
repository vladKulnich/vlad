import  math 
a=float(input("Введіть   число a  "))
b=float(input("Введіть   число b  "))
h=float(input("Введіть   число h  "))
ss=[]
def ff(x):
    z=math.log10(math.fabs(x+math.sqrt(x)))
    return(z)
if a==0 :
    print("обрахування неможливо")
else:
    for i in range (100):
      y= ff(a)
      a= round(a,2)
      y= round(y,4)
      ss.append(y)
      a=a+h
      if a>b:
         break
    r=max(ss)
    t=min(ss)
    ind1 =ss.index(r)
    ind2 =ss.index(t)
    print(ss)
    print ("найбільше значення у списку:" ,r,"",ind1, " по порядку у списку" )
    print ("найменше значення у списку:" ,t,"",ind2, " по порядку у списку" )