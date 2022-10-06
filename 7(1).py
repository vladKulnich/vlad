a=str(input("Введіть  рядок "))
print("всього символів ",len(a))
s=list(a)
n=0
i=0
q=0
while n<len(a):
    if s[n].isdigit() :
        i=i+1
    elif s[n].isalpha() :
        q=q+1
    n=n+1    
print("цифр ", i)
print("букв ",q)
