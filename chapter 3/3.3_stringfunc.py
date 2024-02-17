#  string function

name="rameshrajesh"
print(len(name))

print(name.endswith("bu"))
print(name.startswith("wuoi"))

print(name.count('a'))
print(name.count('r'))
print("this is capitalize")
print(name.capitalize())

print(name.replace("babu","hari"))

print(name.find('rajesh'))

#  chain replace

str_1=input("ramesh")
print(str_1)

date=input("enter the date")

print(date)

template='completed my schooling in tiruppur'

print(template.replace("my",name).replace("in",date))