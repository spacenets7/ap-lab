class ElectricityBill:
    def __init__(self,no=0,name="",units=0):
        self.no=no
        self.name=name
        self.units=units

    def bill(self):
        u=self.units
        return min(u,100)*3+min(max(u-100,0),100)*5+max(u-200,0)*7

    def display(self):
        print(self.no,self.name,self.units,self.bill())

a=ElectricityBill()
b=ElectricityBill(101)
c=ElectricityBill(102,"Arun")
d=ElectricityBill(103,"Meera",250)

for x in [a,b,c,d]:
    x.display()
