a=int(input("enter the number:"))

print(a)

print("the table is")


for i in range(0,11):
# use flower braces for particular print

    print(f"{a}*{i+1}={a*(i+1)}")

else:
    print("the iteartion is finishd")
