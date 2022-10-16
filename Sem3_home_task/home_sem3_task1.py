import random

def random_list (size,array):

    for i in range (size):
        array.append(random.randint(1, 25))
    return array
def sum_arraay_neg_pos (array):
    sum_neg_pos = 0
    for i in range(0,len(array)):
        if i%2!=0:
            sum_neg_pos=sum_neg_pos+array[i]
            print(array[i])
    return sum_neg_pos
try:
    array=[]
    n=int(input("Введите размер списка "))
    random_list(n,array)
    print(array)
    print('На нечетных позициях стоят элемнты: ')
    dig=sum_arraay_neg_pos(array)
    print (f'Сумма элементов на нечетных позициях равна {dig}')
except:
    print("надо было вводить именно целое число")
