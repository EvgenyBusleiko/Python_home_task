import random

def win_count(player_move,total,max_per_turn,x_begin):
    if x_begin==total and x_begin%(max_per_turn+1)!=0:
        best_move=total-(total//(max_per_turn+1))*(max_per_turn+1)
        #print(total//max_per_turn+1)
    elif x_begin==total: best_move=1
    elif x_begin <= max_per_turn :
        best_move = x_begin
    else:
        best_move=max_per_turn+1-(player_move)
    return best_move



print("Игра в конфеты")
print('На столе лежит Х кофет, за один ход можно взять Y шт,но не меньше 1. Кто берет последнюю, тот победил')

x=x_now=int(input("Введите иначальное количество конфет: "))
y=int(input(f'Введите сколько конфет можно брать за ход (не кратное {x}): '))
if x%y==0:
    print(f'{y} кратно {x}, поэтому я прибавил от себя одну конфету')
    x=x_now=x+1
skill=int(input("Хотите играть с умным компьютером (1) или удачливым (2)? : "))


move=random.randint(0,2)
move_player=0

while x_now>0:
    if skill==1:
        if move == 1:
            print(f'На столе сейчас {x_now} конфет')
            print('Ваш ход!')
            move_player = y + 1
            while move_player > y or move_player<1:
                move_player = int(input(f"Сколько конфет берете за ход? (макс = {y}): "))
                if move_player > y or move_player<1: print(f'Нужно вводить число меньше или равное {y}, но больше нуля')
            x_now -= move_player
            move = 0
        else:
            print(f'На столе сейчас {x_now} конфет')
            print('Мой ход!')
            turn = win_count (move_player,x,y,x_now)
            print(f'Я беру {turn} конфет')
            x_now -= turn
            move = 1
    else:
        if move==1:
            print(f'На столе сейчас {x_now} конфет')
            print('Ваш ход!')
            move_player=y+1
            while move_player>y or move_player<1:
                move_player=int(input(f"Сколько конфет берете за ход? (макс = {y}): "))
                if move_player > y or move_player<1: print(f'Нужно вводить число меньше или равное {y}, но больше нуля')
                x_now-=move_player
            move=0
        else:
            print(f'На столе сейчас {x_now} конфет')
            print('Мой ход!')
            if x_now<y:move_player=x_now
            else:move_player = random.randint(1,y)
            print(f'Я беру {move_player} конфет')
            x_now -= move_player
            move = 1
    if x_now==0:
        if move==0 : print('Ты победил, о великий! Все конфеты твои!')
        else: print('Я победил, ничтожный! Все конфеты МОИ !')