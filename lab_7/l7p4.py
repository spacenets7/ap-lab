class Employee:
    def __init__(self,eid,name,basic):
        self.eid=eid
        self.name=name
        self.basic=basic

    def calculate_salary(self):
        return self.basic

class Manager(Employee):
    def __init__(self,eid,name,basic,allowance):
        super().__init__(eid,name,basic)
        self.allowance=allowance

    def calculate_salary(self):
        return self.basic+self.allowance

e=Employee(1,"Arun",30000)
m=Manager(2,"Meera",50000,10000)

print(e.eid,e.name,e.calculate_salary())
print(m.eid,m.name,m.calculate_salary())
