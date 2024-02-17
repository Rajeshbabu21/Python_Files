try :
    n = int(input("enter the number"))
    n1 = int(input("enter th number"))
    res = n/n1
    print(res)
except ZeroDivisionError:
    print("cant be divied")
