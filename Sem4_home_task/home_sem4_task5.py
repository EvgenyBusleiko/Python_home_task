from random import *
import json

city = []

commands =['/start','/add','/all','/stop','/delete','/save','/load','/random']




def save ():
    with open("city.json",'w',encoding='utf-8') as fh:
        fh.write(json.dumps(city,ensure_ascii=False))
        print('Наша база городов была успешно сохранена в файле city.json')
def load ():
    with open("city.json", 'r', encoding='utf-8') as fh:
        city = json.load(fh)
        print('Наша база городов была успешно загружена')

try:
    with open("city.json", 'r', encoding='utf-8') as fh:
        city = json.load(fh)
        print('Наша база городов была успешно загружена')
except:
    city.append("Москва")
    city.append("Смоленск")
    city.append("Санкт-Петербург")
    city.append("Томск")
    city.append("Санта Барбара")
while True:
    print('Сейчас доступны следующие команды')
    print(commands)
    command=input ("Введите команду: ")
    if command=="/start":
        print("Бот-база городов начал свою работу")

    elif command=="/stop":
        print("Бот-база городов остановил свою работу. Заходите еще!")
        save()
        break
    elif command=='/all':
        print('Вот текущий список городов')
        print(city)
    elif command=="/add":
        c=input('Введите названия города: ')
        if not c in city:
            city.append(c)
            print('Город успешно добавлен в коллекцию!')
        else: print('Такой город уже есть в базе')

    elif command == "/help":
        print('Здесь будет какой-то мануал')
    elif command =="/delete":
        c = input('Введите названия города: ')
        try:
            city.remove(c)
            print('Город успешно удален из базы!')
        except:
            print('Такого города нет в базе! ')
    elif command=='/random':

        print(f'Сегодня рекомендуем поехать в {choice(city)}')
    elif command=='/save':
        save()
    elif command=='/load':
        with open("city.json", 'r', encoding='utf-8') as fh:
            city = json.load(fh)
            print('Наша база была успешно загружена')

    else: ("Неопознная команда. Просьба изучить мануал через /help")