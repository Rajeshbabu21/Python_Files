# it will execute after the iteration is fully completed

mylist=[1,2,3,4,5,6,7,8,9,0]
i=1
for item in  range(len(mylist)):
    print(item)
    if(item==7):
        break
    print("the iteration is continued")
else:
    print("the iteration has been stopped")