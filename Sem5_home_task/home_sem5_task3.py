text=input("Введите строку для анализа: ")
text_to_del=input("Введите подстроку для удаления: ")

words_lits=text.split()
#print(words_lits)
for i in range (len(words_lits)-1,-1,-1):
    if text_to_del in words_lits[i]:
        words_lits.pop(i)


new_text=''
for i in words_lits: new_text+=i+' '
print(new_text)

