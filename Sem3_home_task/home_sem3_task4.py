def to_dec (digital):

    if digital==0: return array
    dig=digital%2
    array.append(dig)
    to_dec(digital//2)
try:
    n=int(input("Введите число "))
    array =[]
    to_dec(n)
    array.reverse()
    s=''
    for i in array:
        s=s+str(i)
    print(f'Двоичная форма числа {n}  = {s}')
except:
    print("надо было вводить именно целое число")
