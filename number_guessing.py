
print(' Are you ready to play this game : press Y button to begin: ')
name= input('Enter your name: \n')
print('Hello', name, ', let\'s begin! the number lies between 0 and 10 ')
num= int(input('what is this number: '))

if num > 7:
    if num == 7:
        print('Congratulation, you got it, the number is 7')
    else:
        print('you are wrong, but it comes close')
        num= int(input('try a nother one, to make it is easy, this number is odd one : '))
        if num== 8 :
            print('It was your last trial, the number is 7, good luck next time')
        
    

elif num < 6 and num > 4:
    print('It is your last trial, Be careful, the number is odd and greater than your last choice')
    if num == 7:
        print('Congratulation, you finally got it, the number is 7')
    else:
        print('Good luck next time')

else: 
    print('you are wrong, begin the game again')


