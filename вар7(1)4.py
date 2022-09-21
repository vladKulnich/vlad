import math
x=float(input("введіть x:"))
y=math.pow(math.e, x**2) /math.cos(x+math.pow(x,4))-(x + x**3)**1/4
print (y)