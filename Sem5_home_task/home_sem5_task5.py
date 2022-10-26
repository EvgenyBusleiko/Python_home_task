list=[1, 5, 2, 4,  1, 6, 8 , 15 , 1 ]

chain_lenght=[]


for i in range(len(list)):
    j=1;
    while j<len(list):
        if list[i]+j in list: j+=1
        else:
            chain_lenght.append(j)
            break

max=chain_lenght[0]
max_index=0
for i in range (1,len(chain_lenght)):
    if chain_lenght[i]>max:
        max=chain_lenght[i]
        max_index=i


if chain_lenght[max_index]==1: print('В данном списке цепочек нет')
else: print (f'{list}->[{list[max_index]}, {list[max_index]+chain_lenght[max_index]-1}]')


