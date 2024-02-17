# # f = open("raj.txt","w")
# # f.write("rajesh"+"\n")
# # f.write("hari"+"\n")
# # f.write("rash"+"\n")
# # f=open("raj.txt","r")

# # dict={}
# # data=f.read()
# # for i in data:
    
# #     if i not in dict:
# #         dict[i]=1
# #     else:
# #         dict[i]+=1
# # print(dict) 
# # f.close()

# # reverse
# # f=open("raj.txt","r")
# # data=f.readlines()
# # for j in data:
# #     print(j[::-1])
# # f.close()

# # f=open("raj.txt","r")
# # dat=f.read()
# # print(dat)
# # words=dat.split()
# # lengthw=len(words)
# # print(lengthw)
# # char=len(dat)
# # print(char)
# # line=dat.splitlines()
# # print(len(line))
# # f.close()

# # n=int(input("enter the number"))
# # f=open("raj.txt","r")
# # data=f.readlines()
# # print(data)
# # j=0
# # for i  in data:
# #     if j<n:
# #         print(i[::-1])
# #         j=j+1

# dict={}
# key=input("enter the key")
# while key !="enough":
#     value=int(input("ente the value"))
#     dict[key]=value
#     name=input("enter the name")
# key=input("enter the name")
# if key not in dict:
#     print("not prsent")
# else:
#     print(dit[key]) 
d={}
key=input("Enter student name : ")
while key!='enough':
     value=input("Enter student marks : ")
     d[key]=value
     key=input("Enter student name : ")
key=input("Enter student name : ")
if key not in d:
    print("Key not prsent in dict")
else:
    print(d[key])
choice='yes'
while choice!='no':
    a=input("enter the key to be change : ")
    if key not in d:
       print("Key not prsent in dict")
    else:
       b=input("Enter the new value : ")
       d[a]=b
    choice=input("do you want to continue (yes/no) : ")
print(d)