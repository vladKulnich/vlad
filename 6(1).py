import  math 
a=float(input("Введіть   число a  "))
b=float(input("Введіть   число b  "))
h=float(input("Введіть   число h  "))
def ff(x):
    z=math.log10(math.fabs(x+math.sqrt(x)))
    return(z)
for i in range (100):
    y= ff(a)
    a= round(a,1)
    print(i,'   ',a,'    ',y  )
    a=a+h
    if a>b:
        break