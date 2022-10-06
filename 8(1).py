from array import*
a=(input("Введіть цілі цифри через пробіл "))
s=a.split(' ')
s1=[]
for  n in s:
    s1.append(int(n))
masiv1=array('i',s1)
print(masiv1)
b=sum(masiv1)
print(b/len(s))
