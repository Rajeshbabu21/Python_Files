import random

list=["rajesh","ramesh","hari","sumathi"]
choice=random.choice(list)
print(choice)
print(choice, "has to pay the bill")

if(choice=="rajesh"):
    print("rajesh has to pay the bill")

elif(choice=="ramesh"):
    print("ramesh has to pay the bill")

elif(choice=="hari"):
    print("hari has to pay the bill")

elif(choice=="sumathi"):
    print("sumathi has to pay the bill")


