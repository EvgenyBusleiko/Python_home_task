def operation(text):
    count_add = count_mult=0
    for i in text:
        if i == '*' or i == '/':
            count_mult = count_mult + 1
        elif i == '+' or i == '-':
            count_add = count_add + 1
    for j in range(count_mult):
        sum = 0
        for i in range(len(text) - 1):
            if text[i] == '*':
                sum = int(text[i - 1]) * int(text[i + 1])
                text = text[0:(i - 1)] + str(sum) + text[(i + 2):]
                break
            elif text[i] == '/':
                sum = int(text[i - 1]) // int(text[i + 1])
                text = text[0:(i - 1)] + str(sum) + text[(i + 2):]
                break

    for j in range(count_add):
        sum = 0
        for i in range(len(text) - 1):
            if text[i] == '+':
                sum = int(text[i - 1]) + int(text[i + 1])
                text = text[0:(i - 1)] + str(sum) + text[(i + 2):]
                break
            elif text[i] == '-':
                sum = int(text[i - 1]) - int(text[i + 1])
                text = text[0:(i - 1)] + str(sum) + text[(i + 2):]
                break

    return text

text_to_count=text1=input("Введите выражение для решения: ")
if '(' in text_to_count:
    begin_pos=text_to_count.index('(')
    end_pos=text_to_count.index(')')
    cut_text=text_to_count[begin_pos+1:end_pos]
    if begin_pos==0:
        text_to_count=operation(cut_text)+text_to_count[end_pos+1:]
    else:
        text_to_count=text_to_count[:begin_pos]+operation(cut_text)+text_to_count[end_pos+1:]

result=operation(text_to_count)
print(text1+" = "+result)
