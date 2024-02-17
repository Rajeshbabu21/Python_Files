# f = open("we.txt",'r')
# n = int(input("ente the number"))
# data = f.readlines()
# j=0
# for i in data:
#     if j<n:
#         print(i[::-1])
#     else:
#         print(i)
#     j+=1


f = open("we.txt",'r')
data = f.read()
print(data)
count = len(data)
print(count)
words = len(data.split())
print(words)
lines = len(data.splitlines())
print(lines)
