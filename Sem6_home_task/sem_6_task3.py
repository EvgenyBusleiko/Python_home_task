import re
def input_field():

    check = False
    move = 'a'
    while check == False:
        for i in move:

            if i.isdigit() != True:
                check = False

                if not move == 'a': print('Недопустимые символы')
                move = input("Введите количество игр: ")

                break
            else:
                check = True

    return move

print ('Добрый день!')
qt_games= input_field()
team=[]
huh=[]
teams={}
team_name=[]
for i in range (int(qt_games)):
    text=input('Введите результат матча: ')
    tmp=text.split(';')


    team_name.append(tmp[0])
    team_name.append(tmp[2])
    goal_1=int(tmp[1])
    goal_2=int(tmp[3])
    if goal_1<goal_2:
        tmp_team = team_name[0]
        team_name[0] = team_name[1]
        team_name[1] = tmp_team
    if goal_1 > goal_2:


        team.append(1)
        team.append(1)
        team.append(0)
        team.append(0)
        team.append(3)
        team.append(1)
        team.append(0)
        team.append(1)
        team.append(0)
        team.append(0)
    if goal_1 == goal_2:

        team.append(1)
        team.append(0)
        team.append(0)
        team.append(1)
        team.append(1)
        team.append(1)
        team.append(0)
        team.append(0)
        team.append(1)
        team.append(1)
    else:

        team.append(1)
        team.append(1)
        team.append(0)
        team.append(0)
        team.append(3)
        team.append(1)
        team.append(0)
        team.append(1)
        team.append(0)
        team.append(0)


    # print(team_name[0], team[0:5])
    # print(team_name[1], team[5:10])
    for k in range (2):

        if not(team_name[k]) in teams.keys():
            if k == 0:teams [team_name[k]] = team [0:5]
            else: teams [team_name[k]] = team [5:10]

        else:
            huh=teams.pop(team_name[k])
            if k==0:
                for j in range (len(huh)):
                    team[j]=huh[j]+team[j]
                teams[team_name[k]] = team [0:5]

            else:

                for j in range (len(huh)):
                    team[5+j]=huh[j]+team[5+j]
                teams[team_name[k]] = team [5:10]

    team.clear()
    team_name.clear()
    # print(teams)


    for key,value in teams.items():
        s = ''
        for i in value:
            s=(s+str(i)+' ')
        print (key, ':', s)





# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# import re
# text = """100 ИНФ Информатика
# 213 МАТ Математика
# 156 АНГ Английский"""
# # извлечь все номера курсов
# ch = re.findall('[0-9]+', text)
# # извлечь все коды курсов (для латиницы [A-Z])
# codes = re.findall('[А-ЯЁ]{3}', text)
# # извлечь все названия курсов
# names = re.findall('[а-яА-ЯёЁ]{4,}', text)
# print (ch)
# print(codes)
# print(names)