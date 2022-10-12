import random
from datetime import datetime

left=[]
right=[]
choise_of =[True,False]
before_time=datetime.now()
for i in range (100):
    n=random.randint(5, 25)
    for j in range (n):
        left.append(random.choice(choise_of))
        right.append(random.choice(choise_of))
    left_side=left[0]
    right_side=right[0]
    for j in range(1,n):
        left_side=left_side or left[j-1] or left[j]
        right_side=not(right_side) and not(right[j-1]) and not(right[j])
    if not (left_side)==right_side: print ('Yes')
after_time=datetime.now()


print(f'Программа работала {after_time-before_time}')