f = open("hari.txt","w")
f.write("rajeshr")
f = open("hari.txt","r")
data = f.read()
print(data)
dict = {}
for i in data:
    if i not in dict:
        dict[i] = 1
    else:
        dict [i] = dict[i] +1
print(dict)
f.close() 