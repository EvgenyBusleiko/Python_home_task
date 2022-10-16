import random

def random_list (size,array):

    for i in range (size):
        array.append(random.randint(1, 25))
    return array

def mult_array_pairs (array):
    if len(array)%2==0: len_array=len(array)//2
    else: len_array=len(array)//2+1
    for i in range(0,len_array):
        pairs_array.append(array[i]*array[len(array)-1-i])
    return pairs_array

try:
    array=[]
    n=int(input("Введите размер списка "))
    random_list(n,array)
    print(array)
    pairs_array=[]
    mult_array_pairs(array)
    print (pairs_array)
except:
    print("надо было вводить именно целое число")