array=[]
try:
    n=k=int(input("Введите натуральное число N "))

    while (k>=2):
        for j in range (2,n+1):
            if (k%j==0):
                k=k//j
                array.append(j)
                break

    if len(array)==1: print('Это простое число, делится только на еденицу и себя')
    else: print (f'Число {n} раскладывается на простые множители {array} ')
except:
    print("надо было вводить именно целое число")
