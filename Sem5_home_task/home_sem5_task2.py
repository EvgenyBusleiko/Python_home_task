# def load ():
#     with open("text.json", 'r', encoding='utf-8') as fh:
#         text = json.load(fh)
#         print('Я успешно загрузил из файла следующую информацию')
#         print(text)
# def save ():
#     with open("zip.json",'w',encoding='utf-8') as fh:
#         fh.write(json.dumps(zip,ensure_ascii=False))
#         print('Я успешно загрузил из файла следующую информацию')
#         print(zip)
#

text=input("Введите строку для кодирования: ")
zip=''
i=0
while i <(len(text)):
    count = 1
    tmp=text[i]
    while (i <(len(text)-1)) and (text[i]==text[i+1]):

        count=count+1
        i=i+1
    else: i=i+1
    if count>1:zip=zip+tmp+str(count)
    else:zip=zip+tmp

with open("zip.txt",'w',encoding='utf-8') as fh:
    fh.write(zip)

    print('Я успешно загрузил в файл следующую информацию')
    print(zip)

with open("zip.txt", 'r', encoding='utf-8') as fh:
    zip = fh.read()
    print('Я успешно загрузил из файла следующую информацию')
    print(zip)


text=''

for i in range (len(zip)-1):

    if (zip[i]).isdigit()!=True:
        if (zip[i + 1]).isdigit() == True:
            tmp=int(zip[i+1])
            #print(tmp)
            text = text + zip[i] * tmp

        else:
            text = text + zip[i]

        i=i+1
if (zip[-1]).isdigit()!=True: text=text+zip[-1]
print('После декодирования получаем:')
print(text)