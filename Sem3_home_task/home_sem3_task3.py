import random


def random_list_float (size,array):

    for i in range (size):
        array.append(random.randint(10,1100)/100)
    return array

def find_min_max (array):
    min=max=array[0]%1
    for i in range (1,len(array)):
        if array[i]%1>max:max=array[i]%1
        if array[i]%1 < min: min =array[i]%1
    differ = max  - min

    return differ

array=[]
n=int(input("Введите размер списка "))
random_list_float(n,array)
print(array)
result=round (find_min_max (array)*100)/100
print (f'Разность между максимальной и минимальной дробной частью =  {result}')
