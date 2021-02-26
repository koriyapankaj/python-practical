# welcome to the chapter 4 practical 13
from random import randint

print('+++++++++++++++++++======Let\'s play Rock-Paper-Scissors ========++++++++++++++++')

print('to continue: press any key...')
input()

u_ratio=0
cpu_ratio=0
for i in range(5):
    cpu_guess=randint(1,3)
    cg=0
    if cpu_guess == 1:
        cg='rock'
    elif cpu_guess == 2:
        cg='paper'
    elif cpu_guess == 3:
        cg='scissors'
    user_guess=input('input your move :rock, paper, scissors or R,P,S').upper()
    if (user_guess == 'R' or user_guess == 'ROCK') and (cpu_guess == 1) or (user_guess == 'P' or user_guess == 'PAPER') and (cpu_guess == 2) or (user_guess == 'S' or user_guess == 'SCISSORS') and (cpu_guess == 3):
        
        print(f'!!! tie this round...  user :{user_guess}  ::: cpu :{cg}')
    elif (user_guess == 'R' or user_guess == 'ROCK') and (cpu_guess == 2) or (user_guess == 'P' or user_guess == 'PAPER') and (cpu_guess == 3) or (user_guess == 'S' or user_guess == 'SCISSORS') and (cpu_guess == 1):
        print(f'!!! you lose this round...  user :{user_guess}  ::: cpu :{cg}')
        cpu_ratio+=1
    elif (user_guess == 'R' or user_guess == 'ROCK') and (cpu_guess == 3) or (user_guess == 'P' or user_guess == 'PAPER') and (cpu_guess == 1) or (user_guess == 'S' or user_guess == 'SCISSORS') and (cpu_guess == 2):
        print(f'you win this round!!  user :{user_guess}  ::: cpu :{cg}')
        u_ratio+=1
    else:
        print('invalid input')
        

if cpu_ratio == u_ratio:
    print(f'tie....  user :{u_ratio}  ::: cpu :{cpu_ratio}')
elif cpu_ratio > u_ratio:
    print(f'you lose ...better luck next time !!!!!!   user :{u_ratio}  ::: cpu :{cpu_ratio}')
else:
    print(f'congratulations......you won..  user :{u_ratio}  ::: cpu :{cpu_ratio}')

