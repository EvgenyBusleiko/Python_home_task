def x_diif(text):

    x_x=[0,0,0,0]
    for i in range(len(text)):
        if text[i]=='x':

            if i==0:x_x[3]=1
            elif (text[i-1])=='*' and (text[i+1]=='^'):
                tmp=int(text[i+2])

                x_x[tmp]=int (text[i-2])
            elif ((text[i-1])=='*') and ((text[i+1]=='+') or (text[i+1]=='-')):
                x_x[1]=int (text[i-2])

    if text[-1]!='x':x_x[0]=int(text[-1])

    print(x_x)
    return x_x


yravn = []

yravn.append('5*x^3+2*x^2+6')
yravn.append('7*x^2+6*x+3')
yravn.append('x^3+2*x^2+4')
sum =[]
print('Исходные уравнения:')
for i in range(len(yravn)):
    print(yravn[i])
    sum.append(x_diif(yravn[i]))


#print(sum)
total=[]
for i in range (4):
    total.append(sum[0][i]+sum[1][i]+sum[2][i])
#print(total)

print(f'Итоговая сумма двух уравнений будет {total[3]}*x^3+{total[2]}*x^2+{total[1]}*x+{total[0]}')