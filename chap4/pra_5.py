# welcome to the chapter 4 practical 5

from random import randint

flag=randint(1,10)

choice=int(input('Enter your guess'))
if flag == choice:
    print('your guess is right !!!')
else:
    print('number is ',flag,'better luck next time')



