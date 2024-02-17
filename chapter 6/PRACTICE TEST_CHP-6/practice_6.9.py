height=float(input("enter the height"))
print(height)

weight=int(input("enter the weight"))
print(weight)

bmi=weight/(height**2)

print(int(bmi))

if(bmi<16.0):
    print("under weight")

elif(bmi>=16.0 or bmi<=16.9):
    print("moderate thinness")

elif(bmi>=17.0 and bmi<=18.4):
    print("mild thinness")

elif(bmi>=18.5 or bmi<=24.9):
    print("normal range")

elif(bmi>=25.0 or bmi<=29.9):
    print("pre obese")

elif(bmi>=30.0 or bmi<=34.9):
    print(" ob clss 1")

elif(bmi>=35.0 or bmi<=39.9):
    print("ob class 2")

elif(bmi>=40.0):
    print("ob class 3")

else:
    print("not considered")

       