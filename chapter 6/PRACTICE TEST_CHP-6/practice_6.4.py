mark_1=int(input("enter the number"))
print(mark_1)

if(mark_1>=90 or mark_1==100):
    print("ex")
elif(mark_1>=80 or mark_1==90):
    print("A")    
elif(mark_1>=70 or mark_1==80):
    print("B")    
elif(mark_1>=60 or mark_1==70):
    print("C")    
elif(mark_1>=50 or mark_1==60):
    print("D")
elif(mark_1<50):
    print("F")   
else:
    print("fail")                      