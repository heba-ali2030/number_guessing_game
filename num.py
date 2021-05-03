print(' Are you ready to play this game : press Y button to begin: ')
name= input('Enter your name: \n')
print('Hello', name, ', let\'s begin! the number lies between 0 and 10 ')
num= int(input('what is this number: '))

for i in range(0,10):
    if num== 7:
        print('Congratulation, you got it, the number is 7')
        break
    
    
    else:
        print('you are wrong, but it comes close')
        num= int(input('try a nother one, to make it is easy, this number is odd one : '))
    