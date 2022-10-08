try:
    x=float(input("Введите первое число "))
    y=float(input("Введите второе число "))
except:
    print("Ошибка ввода")
action = input("Введите код действия (+,-,*,/,mod,pow,div) ")
if (y==0) and ((action=='div') or (action=='/') or (action=='mod')):
    print ("Деление на ноль!")
elif (action=='+'):
    print (f"{x} {action} {y} ={x+y}")
elif (action=='-'):
    print (f"{x} {action} {y} ={x-y}")
elif (action=='*'):
    print (f"{x} {action} {y} ={x*y}")
elif (action=='/') and (y!=0):
    print (f"{x} {action} {y} ={x/y}")
elif (action=='mod') and (y!=0):
    print (f"{x} {action} {y} ={x%y}")
elif (action=='pow'):
    print (f"{x} {action} {y} ={x**y}")
elif (action=='div') and (y!=0):
    print (f"{x} {action} {y} ={x//y}")


