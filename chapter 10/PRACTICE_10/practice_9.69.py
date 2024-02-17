class sheet:
    def __init__(self):
        self.name = ""
        self.roll=0
        self.marks=0
    def inp(self):
        self.name = input("Enter your name: ")
        self.roll = int(input("Enter your roll number: "))
        n=int(input("enter the number of marks"))
        for i in range(1,n+1):
            self.marks=int(input("ente rthe marks"))
class total_sheet(sheet):
    def __init__(self):
        super().__init__()
        self.total=0
        self.avg=0
    def value(self):
        self.inp()
        print("the total is",self.total)
        print("the average is",self.avg)

sheet=total_sheet()
sheet.value()

    
