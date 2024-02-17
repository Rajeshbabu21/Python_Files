mark_1=int(input("enter the 1st subject mark :"))
mark_2=int(input("enter the 2st subject mark :"))
mark_3=int(input("enter the 3st subject mark :"))

print(mark_1,mark_2,mark_3)

if(mark_1>40 and mark_1>33):
    print("the is first subject is pass")
else:
    print("fail")

if(mark_2>40 and mark_2>33):
    print("the second subject is pass")
else:
    print("fail")

if((mark_3>40 and mark_3>33)):
    print("the third subject is passed")
else:
    print("fail")


