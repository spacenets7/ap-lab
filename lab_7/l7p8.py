class Person:
    def __init__(self,name,**kwargs):
        super().__init__(**kwargs)
        self.name=name

    def display_role(self):
        print(self.name,"Person")

class Student(Person):
    def __init__(self,reg=None,**kwargs):
        super().__init__(**kwargs)
        self.reg=reg

    def display_role(self):
        print(self.name,"Student")

class Employee(Person):
    def __init__(self,eid=None,**kwargs):
        super().__init__(**kwargs)
        self.eid=eid

    def display_role(self):
        print(self.name,"Employee")

class TeachingAssistant(Student,Employee):
    def display_role(self):
        print(self.name,"Teaching Assistant")

p=Person(name="Arun")
s=Student(name="Meera",reg="2301")
e=Employee(name="Ravi",eid="E01")
t=TeachingAssistant(name="Anu",reg="2302",eid="E02")

for x in [p,s,e,t]:
    x.display_role()

print(TeachingAssistant.mro())
