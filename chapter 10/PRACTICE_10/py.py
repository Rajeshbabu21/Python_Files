class employee:
    def __init__(self):
        self.name=""
        self.age=0
        self.salary=0
        
    def get_employee(self):
        self.name=input("enter the name")
        self.age=int(input("enter the age"))
        self.salary=int(input("enter the salary"))
    def print1(self):
        
        print("the name is",self.name)
        print("the age is",self.age)
        print("the salary is",self.salary)
        
    def get_salary(self):
        return self.salary
    
class perks(employee):
    def __init__(self):
        super().__init__()
        self.hra=0
        self.ta=0
        self.da=0
    def get_allowance(self):
        self.hra=self.salary*0.20
        self.ta=self.salary*0.30
        self.da=self.salary*0.40
    def put_allowance(self):
        self.get_allowance()
        self.print1()
        print("the hra is",self.hra)
        print("the ta is",self.ta)
        print("the da is",self.da)

employee=perks()
employee.get_employee()
employee.put_allowance()
        
        
