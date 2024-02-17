def largest(a,b,c):
    if a>b and a>c:
        print("a is largest")
    elif b>c:
        print("b is largest")
    else:
        print("c is largest")

a = int(input("enter the number"))
b = int(input("enter the number"))
c = int(input("enter the number"))

largest( a,b,c)