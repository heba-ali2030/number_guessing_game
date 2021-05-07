print(f'Are you ready to play this game : press Y button to begin: ')
name = input('Enter your name: \n')
print(f'Hello', name, ', let\'s begin! the number lies between 0 and 10 ')

num= int(input('what is this number: '))

import random

num2 = random.randint(0,10)
print(num2)
    
    
while num != num2:
    print('you are wrong, but it comes close')
    
    if num2 % 2 ==0:
        print('To make it easy , the number is even one')
    
    else:
        print('To make it easy , the number is odd one')
    num = int(input('try a nother one, what is your guess? '))

else:
    print('Congratulation, you got it, the number is: ',num2)