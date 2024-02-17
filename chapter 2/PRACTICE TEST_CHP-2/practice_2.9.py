n = int(input("enter thr number"))
sum = 0
for i in range(150, n+1):
    temp = n
    while temp > 0:
        digit = temp%10
        sum +=digit**3
        temp = temp//10
        print(sum)
if n == sum:
    print("mam")
else: 
    print("not a amsrtrong")  