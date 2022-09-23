import  math 
x=float(input("Введіть  число x:"))
if x>= -0.7 :
    z=-6*x**2+math.sin(x)
elif x>-9.9 :
    z=math.log10(math.fabs(x+math.sin(x)))
elif x<=-9.9:
    z=12+math.fabs(math.sin(2*x))
print(z)
    
