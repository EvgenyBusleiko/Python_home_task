def output_x2 (s,symb):
    cut = ''
    for i in range (len(s)):
        if s[i]==symb:
            if i==0:
                cut=''
                break
            else:
                cut=s[0:i-1]
                break


    s=s[i+1:]
    if cut=='-':
        x=-1
        return x, s
    elif  cut=='':
            x=1
            return x, s
    else : x=int(cut)
    return x,s
def output_x (str_1,symb):
    cut = ''

    for i in range (len(str_1)):
        if str_1[i]=="-" or str_1[i]=="+" :

            break
    for j in range(i,len(str_1)):
        if str_1[j]==symb:
            cut=str_1[i:j-1]
            break

    str_1=str_1[j+1:]
    x=int(cut)

    return x,str_1
def output_c (str_1,symb):
    cut = ''

    for i in range(len(str_1)):
        if str_1[i] == "-" or str_1[i] == "+":
            break
    for j in range(i, len(str_1)):
        if str_1[j] == symb:
            cut = str_1[i:j]
            break

    x = int(cut)

    return x

str=input("Введите квадратное урaвнение вида A*x^2+B*x+C=0 ")

x_x=output_x2(str,'x')
a=x_x[0]
x=output_x (x_x[1],'x')
b=x[0]
c=output_c (x[1],'=')

print(f'a={a},b={b},c={c}')

d=b**2-4*a*c


x_1=-b+d**0.5/2*a
x_2=-b-d**0.5/2*a

if (d<0): print("Нет корней в области вещественных чисел")
elif (d>0):print(f'Корни равны {x_1} и {x_2}')
else: print(f'Оба корня равны {x_1}')