# welcome to the chapter 4 practical 10
from random import randint
print('=====++++++++  Let\'s play math game ++++++++===========\n\n')
print('::i will ask you 10 qustions\n')

input('Press any key to continue ......')

for i in range(10):
    a=randint(1,9)
    b=randint(1,9)
    print(f'Question {i+1} : {a} x {b} = ',end='')
    c=int(input())
    ans=a*b
    if c == ans:
        print('Right !')
    else:
        print('wrong ! right answer is :',ans)



