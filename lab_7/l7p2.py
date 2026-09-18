class Employee:
    def __init__(self,eid,name,basic):
        self.eid=eid
        self.name=name
        self.basic=basic
        self.gross=basic*1.3

    def display(self):
        print(self.eid,self.name,self.basic,self.gross)

e=[]
for _ in range(5):
    eid=input("ID: ")
    name=input("Name: ")
    basic=float(input("Basic salary: "))
    e.append(Employee(eid,name,basic))

for x in e:
    x.display()

h=max(e,key=lambda x:x.gross)
print("Highest:",h.eid,h.name,h.gross)

key=input("Search ID: ")
f=next((x for x in e if x.eid==key),None)
f.display() if f else print("Not found")
