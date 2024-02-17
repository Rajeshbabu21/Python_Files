f = open("this.txt", "r")
text = f.read(6)
text = f.readline()
print(text)

print("hi")
# return string in the list
text_list = f.readlines()
print(text_list)
f.close()