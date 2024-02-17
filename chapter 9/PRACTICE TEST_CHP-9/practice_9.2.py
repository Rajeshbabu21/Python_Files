# # with open("rajesh.txt", 'w') as f:
# #     f.write("bsfnbss\njdasdjan\ndsdjs\n")
# #     data =f.read()
# #     print(data)

# f = open("rajesh.txt",'r')
# text = f.read()
# print(text)
# list=[]
# for line in f:
#     list.append(line)
#     print(list)
    
    
# # f.close()
f = open("rajesh.txt",'r')
text = f.read()
print(text)
no_words=len(text.split())
print(no_words)
print(len(text))

f = open("ramesh.txt",'r')
text = f.read()
print(text)
text1 = f.readlines()
print(text1)



f.close()




    