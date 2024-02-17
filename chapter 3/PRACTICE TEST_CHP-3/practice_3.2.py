name="rajesh"
print(name)

date=(input("enter the date"))
print(date)

# print("last sentence")

template="dear <name> you are selected <date>"

print(template.replace("<name>",name).replace("<date>",date))


