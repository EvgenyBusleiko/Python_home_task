import random
def random_matrix (size_x, size_y):
    array = [[random.randint(1, 100) for j in range(size_x)] for i in range(size_y)]
    return array
def print_matrix (array):
    for i in array:
        for j in i:
            print(j,end=' ')
        print()
def mix_matrix (array):
    array_simple=[]
    array_check=[]

    for i in array:
        for j in i:
            array_simple.append(j)
            array_check.append(False)


    for i in range(len(array_simple)-1):
        if array_check[i]==False:
            array_check[i]=True
            j=i
            while array_check[j]==True:
                j=random.randint(i+1,len(array_simple)-1)
            tmp=array_simple[i]
            array_simple[i]=array_simple[j]
            array_simple[j]=tmp
            array_check[j]=True

    k=0
    for i in range (len(array)):
        for j in range (len(array[i])):
            array[i][j]=array_simple[k]
            k=k+1
    return array
try:
    n=1
    m=1
    while ((n*m)%2!=0):
        n = int(input("Введите четное число строк списка: "))
        m = int(input("Введите четное число столбцов списка: "))
        if (n*m)%2!=0: print('Нужно чтобы общее число элементов было четным')
    matrix=random_matrix(n,m)
    #matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print("Матрица ДО перестановки")
    print_matrix(matrix)
    print("Матрица ПОСЛЕ перестановки")
    print_matrix(mix_matrix(matrix))
except:
    print("надо было вводить именно целое число")