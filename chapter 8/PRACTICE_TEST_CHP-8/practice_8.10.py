number = int(input("enter the number"))
print(number)

def prime(number):
    for i in range(1,number):
        
        if number%i==0:
            print("it is  not prime number")
            break
        else:
            print("it is a prime")

prime(number)            

















