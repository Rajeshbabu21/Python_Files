no = int(input("enter the number"))
i = 0
while i <no:
    class employee():
        def __init__(self):
            self.name = ""
            self.age = 0
            self.salary = 0
        def getemployee(self):
            self.name = input("enter thr nqm")
            self.age = int(input("enter the age"))
            self.salary = float(input("enter salary"))
        def printemployee(self):
            print("Name:",self.name)
            print("Age:",self.age)
            print("Salary:",self.salary)
        def salary(self):
            return self.salary;
    class perks(employee):
    
        def __init__(self):
            super().__init__()
            self.bonus=0
            self.hra=0
            self.pf=0
        def getallowance(self):
            self.bonus = self.salary*0.20
            self.hra = self.salary*0.10
            self.pf = (self.salary * 15)/100
        def putallowance(self):
            self.getallowance()
            print("emp details")
            self.printemployee()
            print("Bonus:",self.bonus)
            print("HRA:",self.hra)
            print("pf",self.pf)
    employee = perks()
    employee.getemployee()
    employee.putallowance()
    i = i+1




