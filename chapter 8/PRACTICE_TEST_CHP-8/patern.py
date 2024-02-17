n = "rajessf"
for i in range(0,len(n)):
    for j in range(0 , i+1):
        print(n[j],end = "")
    print()

n = 5
for i in range(0,n + 1):
    for j in range(0 , i+1):
        print("*",end = "")
    print()


n = "python"
for i in range(0,len(n)):
    for j in range(0 , len(n) - i):
        print(n[j],end = "")
    print()