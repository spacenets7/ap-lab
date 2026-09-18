class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self,name,age,reg,marks):
        super().__init__(name,age)
        self.reg=reg
        self.marks=marks

class Result(Student):
    def __init__(self,name,age,reg,marks):
        super().__init__(name,age,reg,marks)

    def calculate(self):
        self.total=sum(self.marks)
        self.avg=self.total/3
        self.grade="A" if self.avg>=80 else "B" if self.avg>=60 else "C" if self.avg>=40 else "F"

    def display(self):
        print(self.name,self.age,self.reg,self.marks,self.total,self.avg,self.grade)

r=Result("Arun",20,"2301",[78,84,91])
r.calculate()
r.display()
