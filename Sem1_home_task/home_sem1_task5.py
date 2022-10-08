array = [[5, 10, 11, 1], [7, 6, 3, 2]]
array_simple=[]
k=0;
print(array)
for i in range (2):
    for j in range (4):
        array_simple.append(array[i][j])
# print(array_simple)
for i in range (6):
    for j in range (7):
        if (array_simple[j]>array_simple[j+1]):
            temp=array_simple[j]
            array_simple[j]=array_simple[j+1]
            array_simple[j+ 1]=temp
for i in range (2):
    for j in range (4):
        array[i][j]=array_simple[k]
        k=k+1


print(array)