try:
     n=int(input("Введите размер последовательности N "))
     array=[]
     for i in range(n):
          array.append(int(input(f"Введите {i+1}-ый элемент последовательности N ")))
     array_new=[]
     array_new.append(array[0])
     for i in range (1,len(array)):
          for j in range (len(array_new)):
               if array_new[j]==array[i]: break
               if j==len(array_new)-1: array_new.append(array[i])
     # if not (array[i]) in array_new: array_new.append(array[i])
     print (f'Исходный массив {array}')
     print(f'Уникальные элементы {array_new}')
except:
    print("надо было вводить именно целое число")