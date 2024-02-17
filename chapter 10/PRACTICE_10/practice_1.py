a = int(input("enetr the nyjmner"))

print(a)
i = 0
while(i<a):
    
    class mark_sheet():
        def __init__(self):
            self.name = ""
            self.roolno = 0
            self.marks = 0
        # self.total =0
        # self.total_avg = 0

        
        
    def input_details(self):
        self.list = []
        self.name = input("Enter your name: ")
        self.roolno = int(input("Enter your roll number: "))
        
        for i in range(1,4):
            marks = int(input(f"Enter your {i}th subject marks: "))
            self.list.append(marks)
        # print(self.list)

    def total_avg(self):
        self.total = sum(self.list)
        #nnnprint(self.total)
        self.avg = self.total/3

    def grade(self):
        if self.avg >=90 and self.avg <=100:
            print("Grade A")
        elif self.avg >=80 and self.avg <90:
            print("Grade B")
        elif self.avg >=70 and self.avg <80:
            print("Grade c")
        # elif self.avg >=60 and self.avg <70:
        #     print("Grade d")
        else:
            print("d")

    def mark_sheet1(self):
        print("name",self.name)
        print("roll no",self.roolno)
        print("mark1",self.list[0])
        print("mark2",self.list[1])
        print("mark3",self.list[2])
        
        if self.list[0] > 50:
            self.list[1] > 50
            self.list[2] > 50
            print("pass")
        else:
            print("fail")
    object = mark_sheet()
    object.input_details()
    object.total_avg()
    object.grade()
    object.mark_sheet1()
    i=i+1
    

            
        
        