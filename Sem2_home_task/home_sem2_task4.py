n=input ('Введите строку, в которой искать:')
m=input ('Введите строку для поиска:')

count=0;


for i in range (len(n)-len(m)+1):
    if (n[i:i+len(m)]==m): count+=1

if count>0 : print (f'Подстрока "{m}" содержится в "{n}" {count} раз(а)')
else : print (f'Подстрока "{m}" НЕ содержится в "{n}" ')