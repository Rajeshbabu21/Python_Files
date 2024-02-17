no=int(input("enter the number of times"))
i=1
while i<no:
    class student_sheet:
        def __init__(self):
            self.name=""
            self.marks=0
            self.grades=""
            self.rollno=0
            self.avg=0
        
        
        def input_details(self):
            self.list=[]
            self.name=input("enter the name")
            self.rollno=int(input("enter the roll number"))
            print("for  5 subject marks")
            for i in range(1,4):
                self.marks=int(input("enter the marks for 5 subjects"))
                self.list.append(self.marks)
            
        def total(self):
            self.total=(sum(self.list))
            print(self.total)
            self.avg=(self.total/5)
        def grade(self):
            if self.avg>=90 and self.avg<=100:
                self.grades="s"
            elif self.avg>=80 and self.avg<=90:
                self.grades="A"
            else:
                self.grades="fail"
            
        
        def marksheet(self):
            print("the name",self.name)
            print("the roll no",self.rollno)
            print("mark1",self.list[0])
            print("mark2",self.list[1])
            print("mark3",self.list[2])
            print("the total",self.total)
            print("the average is",self.avg)
            print("the grade is",self.grades)
        
            if (self.list[0]>=50 and self.list[1]>=50 and self.list[2]>=50):
                print("pass")
            else:
                print("fail")
              
           

 
    object=student_sheet()
    object.input_details()
    object.total()
    object.grade()
    object.marksheet()
    i = i+1

    
