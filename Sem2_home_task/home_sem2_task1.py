from fractions import Fraction
try:
    dig=Fraction(input("Введите число "))
    x=abs(dig)
    while ((x%10)!=0):

        x=x*10
        print (x)
    sum_of_dig=0;
    while ((x//10)!=0):
        x = x // 10
        sum_of_dig=sum_of_dig+(x%10)


    print (f'сумма цифр числа {dig} = {sum_of_dig}')
except:
    print("Ошибка ввода")