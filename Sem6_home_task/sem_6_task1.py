import random, os

field = []
field_count=[]
def print_field (field_print):
    for i in range(3):
        print("  ".join(field_print[i]))

def input_field():
    check = False
    move = '7'
    while check == False:
        for i in move:
            if i != '0' and i != '1' and i != '2' and i != ',':
                # print(i)
                check = False
                if not move == '7': print('Недопустимые символы')
                move = input("Введите координаты вашего хода через запятую: ")
                break
            else:
                check = True
    return move

def player_move (field_print):
    print('Твой ход')
    move_coord=input_field().split(',')
    x=int (move_coord[0])
    y=int (move_coord[1])
    while field[x][y] != '_':
        print("Поле занято, введите другие координаты")
        move_coord = input_field().split(',')
        x = int(move_coord[0])
        y = int(move_coord[1])
    field [x][y]='X'
    field_count[x][y]=4

def comp_move (field_print):
    print('Мой ход')
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    while field[x][y] != '_':
        x = random.randint(0, 2)
        y = random.randint(0, 2)
    field[x][y]='0'
    field_count[x][y] = 1

def win_check():
    winner=''
    sum=[]
    for i in range (8): sum.append(0)
    tmp=0
    tmp1=0
    for i in range (3):
        for j in range(3):
            tmp=tmp+field_count[i][j]
            tmp1 = tmp1 + field_count[j][i]
            if (i==j):
                sum[6]=sum[6]+ field_count[j][i]

            if ((i==j==1)) or ((i==0) and (j==2)) or ((i==2) and (j==0)):
                sum[7]=sum[7]+ field_count[j][i]

        sum[i] = tmp
        sum[i + 3] = tmp1
        tmp =tmp1=0

    for i in sum:
        if i==3 :winner="Я победил!"
        elif i==12:winner="Ты победил!"

    return winner;




win=''
print('Игра в "крестики-нолики"')

print('Первый ход определяется случайным образом')

print('Компьютер всегда играет ноликами')
input ('Для продолжения нажмите любую клавишу')
# os.system('Clear ')
for i in range (3):
    fieldrow=[]
    field_drow_count=[]
    for j in range (3):
        fieldrow.append ('_')
        field_drow_count.append(0)
    field.append (fieldrow)
    field_count.append(field_drow_count)
print_field(field)

m=random.randint(1,2)

while win=='':
    if m%2==0:
        player_move (field)
        m=m+1
    else:
        comp_move (field)
        m = m + 1
    print_field(field)
    win=win_check()
    if m>10: win="Ничья!"
print(win)


