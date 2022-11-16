class City():
    def __init__ (self,name,country,population): 
        self.name=name
        self.country=country
        self.population=population
    def __del__ (self):
        print("місто вилучено") 
    def change(self):
        newname=s1[0]
        newcountry=s1[1]
        newpopulation=s1[2]
        self.name=newname
        self.country=newcountry
        self.population=newpopulation
        print("добавлено")
    def vuvod(self):
        print("місто ", self.name," ,країна ", self.country, ", населення " ,self.population)
        
kiev=City("Київ","Україна",3000000)
varshava=City("Варшава","Польща",2200000)
london=City("Лондон","Британія",2000000)
s=[kiev,varshava,london]
z=City("","",0)
x=City("","",0)
c=City("","",0)
zxc=[z,x,c]
print("введіть 1 для додання у список об'єта, 2 видалення зі списку міста з заданим іменем,3 виведення об´єкта на екран, 4 виход ")
a=str
i=0
while not a=="4":
    a=(input("Введіть цифру "))
    if a=="1":
        q=(input("введіть дані через кому " ))
        s1=q.split(",")
        zxc[i].change()
        i+=0
        s.append( zxc[i])
        
    elif a=="2":
        q=(input("введіть назву для видалення " ))
        if kiev.name==q:
            s.remove(kiev)
            del kiev
        elif varshava.name==q:
            s.remove(varshava)
            del varshava
        elif london.name==q:
            s.remove(london)
            del london
        elif z.name==q:
            s.remove(z)
            del z
        elif x.name==q:
            s.remove(x)
            del x
        elif c.name==q:
            s.remove(c)
            del c
        else : print("нема такого міста")
    elif a=="3":
        q=(input("введіть назву " ))
        for y in s:
            if y.name==q:
                y.vuvod()
print(s)




        
        



