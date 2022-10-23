import random
try:
    k=int(input("Введите натуральную степень k "))
    s=''
    for i in range(k,-1,-1):
        n=random.randint(0,10)
        if i>1 and n!=0:
            if n!=1:s=s+(f'+{n}*x^{i}')
            else: s=s+(f'+x^{i}')
        elif i==1 and n!=0:
            if n!=1:s=s+(f'+{n}*x')
            else:s=s+(f'+x')
        elif i==0 and n!=0: s=s+(f'+{n}')

    s=s[1:]
    s=(f'{k} -> ')+s
    s=s+'=0\n'


    with open ('file.txt','a') as data:
        data.write(s)
    print(s)
except:
    print("надо было вводить именно целое число")