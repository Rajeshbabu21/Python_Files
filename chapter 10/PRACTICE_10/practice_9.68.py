class employee:
    def __init__(self):
        self.name=""
        self.age=0
        self.salary=0

    def inp(self):
        self.name=input("enter the number")
        self.age=int(input("enter the age"))

    def pri(self):
        print("the name is ",self.name)
        print("the age",self.age)

    def perks(self):
        self.hra=self.salary*0.20
        self.ta=self.salary*0.30
        self.da=self.salary+340

    def print1(self):
        print("the hra is",self.hra)
        print("the ta is",self.ta)
        print("the da is",self.da)
obj=employee()
obj.inp()
obj.pri()
obj.perks()
obj.print1()




