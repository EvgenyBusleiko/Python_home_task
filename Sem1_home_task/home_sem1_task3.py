try:
    x=int(input("Введите координату Х "))
    y=int(input("Введите координату Y "))
    if (x>0) and (y>0):
        print ("Это первая плоскость")
    elif (x<0) and (y>0):
        print("Это вторая плоскость")
    elif (x < 0) and (y < 0):
        print("Это третья плоскость")
    else: print ("Это четвертая плоскость")
except:
    print("Ошибка ввода")