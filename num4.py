
print(f'Are you ready to play this game : press Y button to begin: ')
name = input('Enter your name: \n')

first = int(input('enter the first number you want to play: \n first number:  '))
last = int(input('enter the last number of range you want to play: \n last number:  '))

print(f'Hello {name}, let\'s begin! the number lies between {first} and {last}')

num= int(input('what is this number: '))

import random
num2 = random.randint(first, last)
print(num2)

run= 0
while run < 5:
    run += 1
    

    while num != num2:
        print('you are wrong, but it comes close')

        if num < num2:
            print(f'Try Again! You guessed too small')
        
        else:
            print(f' Try Again! You guessed too high')


        num = int(input('try a nother one, what is your guess? '))


    else:
        print(f'Congratulation, you got it, the number is: {num2}')
        break



else:
    print(f'{name}, Sorry \n <<< Game is over, Good luck next time >>>')



