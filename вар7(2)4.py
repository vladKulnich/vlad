import  math 
def func1(x1,x2,x3,x4):
    z=2.33*math.pi*(x1*math.sin(x2)+x2*math.cos(x3)) + math.pow(math.e,x3*x4)
    return(z)
x=float(input("Введіть  число x:"))
y=float(input("Введіть  число y:"))    
a=float(input("Введіть  число a:"))
t=float(input("Введіть  число t:")) 
z=func1(x,y,a,t)
print(z)
