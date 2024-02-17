n = int(input("enter the number"))
m = int(input("enter the nmmer"))
list = []
matrix = []
for i in range(1,n):
    list.append(i)
    print(list)
    for j in range(1,m):
        matrix.append([j])
        print(matrix)

print(list[0] + matrix[0][0])
print(list[1] + matrix[1][0])