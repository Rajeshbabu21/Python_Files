f = open("poem.txt","r")
poem = f.read()
print(poem)

if("star" in f.read()):
    print("it contains")
else:
    print("not contains")