a=int(input("enter the first number :"))
b=int(input("enter the first number :"))
c=int(input("enter the first number :"))
d=int(input("enter the first number :"))

print(a,b,c,d)

if(a>b or a>c or a>d):
    print("a is greater")
elif(b>c or b>d):
    print("b is greater")
elif(c>d):print("c is graeter")
else:
    print("d is greater")    
