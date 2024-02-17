# # import random

# # str=input("enter the string")

# # print(str)

# # splitted=str.split(",")
# # print(splitted)


# # # print(splitted[0])
# # # print(splitted[1])
# # # print(splitted[2])
# # # print(splitted[3])
# # # print(splitted[4])

# # mylist=[splitted[0],splitted[1],splitted[2],splitted[3]]
# # print(mylist)



# # choice=random.choice(mylist)
# # print(choice)
# # print(choice,"has to pay the bill pay")

# # set = {1,2,3,4,54}
# # list_1 = list(set)
# # print(list_1)

# # n = int(input("enter the number"))
# # a= 0
# # b = 1
# # print(a)
# # print(b)
# # for i in range(2,n):
# #     c= a+b
# #     a=b
# #     b=c
# # #     print(c)


# sum = 0
# n = int(input("enter the number"))
# temp = n
# while temp > 0:
#     digit = temp % 10
#     sum = sum + digit**3
#     temp = temp// 10
#     print(sum)

# if n == sum:
#     print('amstrong')
# else:
#     print("not amstrong")


n = int(input("enter the number"))
s = ""
while n>0:
    r = n%2
    s = str(r) + s
    q = n//2
print(int(s))

    
# print("gi \n rajesh")
n = int(input("enter th number"))
n1 = int(input("enter th number"))

if n1 > n1:
    great = n
else:
        greate = n1
while True:
    if (greate % n == 0 and greate % n1== 0):
        lcm = greate
        break
    greate = greate + 1
print (lcm )