class Sweat():
    def __init__ (self,name,price,producer): 
        self.name=name
        self.price=price
        self.producer=producer
    def SetPrice(self,v):
        self.price=v
    def SetName(self,v):
        self.name=v
    def Display (self):
        print("назва ", self.name," ,ціна ", self.price, ",виробник " ,self.producer)
    def GetName(self):
        return(self.name)
    def GetPrice(self):
        return(self.price)


