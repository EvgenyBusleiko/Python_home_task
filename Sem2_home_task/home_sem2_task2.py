try:
    n=int(input ('Введите число N:'))
    spisok=[]
    spisok.append(1)
    for i in range (1,n):
        spisok.append(spisok[i-1]*(i+1))
    print (spisok)

except:
    print("Ошибка ввода")