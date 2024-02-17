def multiplication(number):
  print("the table is ")
  for i in range(1, 111):
     print(f"{number}* {i} = {number * i}")

number = int(input("enter the number"))
print(number)

multiplication(number)