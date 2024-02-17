a=input("enter the amt size")
print(a)
bill=0

if(a=='S'or "s"):
    print("it cost 100")

elif(a=='M' or 'm'):
        print("it cost 200")
else:
    print("it cost 300")

pepper=input("enter the  pepper if yes or no")

if(pepper=='Y' or 'y' ):
     bill=100+30
     print("the bill is for small size ",bill)

elif(pepper=='Y' or 'y'):
     bill= 200+50
     print("the bill is for medium size pizza",bill) 

            
