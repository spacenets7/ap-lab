class Student:
    def accept(self):
        self.reg=input("Register No: ")
        self.name=input("Name: ")
        self.marks=list(map(float,input("Enter 3 marks: ").split()))

    def calculate(self):
        self.total=sum(self.marks)
        self.avg=self.total/3
        self.result="Pass" if all(m>=40 for m in self.marks) else "Fail"

    def display(self):
        print(self.reg,self.name,self.marks,self.total,self.avg,self.result)

s=Student()
s.accept()
s.calculate()
s.display()
