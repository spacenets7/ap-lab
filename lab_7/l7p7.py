class Academic:
    def __init__(self,marks):
        self.marks=marks

    def total(self):
        return sum(self.marks)

class Sports:
    def __init__(self,score):
        self.score=score

class StudentResult(Academic,Sports):
    def __init__(self,reg,name,marks,score):
        Academic.__init__(self,marks)
        Sports.__init__(self,score)
        self.reg=reg
        self.name=name

    def display(self):
        a=self.total()
        print(self.reg,self.name,a,self.score,a+self.score)

s=StudentResult("2301","Arun",[80,75,90],20)
s.display()
