import  math 
a=float(input("Введіть   число a  "))
b=float(input("Введіть   число b  "))
h=float(input("Введіть   число h  "))
n=1
def ff(x):
    z=math.log10(math.fabs(x+math.sqrt(x)))
    return(z)
while a<b:
    y= ff(a)
    a= round(a,2)
    y= round(y,4)
    print(n,'   ',a,'    ',y  )
    a=a+h
    n=1+n