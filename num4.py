
# begin the game and ask the user to press yes to continue

print(f'Are you ready to play this game : press Y button to begin: ')
play= input(f' press yes to continue ... no to exit \n ')
if play== 'yes' :





# get user name
    name = input('Enter your name: \n')

# get the number range from the user

    first = int(input('enter the first number you want to play: \n first number:  '))
    last = int(input('enter the last number of range you want to play: \n last number:  '))

# tell the user that range

    print(f'Hello {name}, let\'s begin! the number lies between {first} and {last} \n You have 5 trials')


    user_guess= int(input('what is this number: '))

    import random
    number_to_be_guessed = random.randint(first, last)
    print(number_to_be_guessed)


# Number of times for the guess game to run
    run= 0
    while run <= 5:
    
        run += 1
    
# 1- if the user guess is true
        if user_guess == number_to_be_guessed:
            print(f'Congratulation, you got it, the number is: {number_to_be_guessed}')
            break
# 2- if the guess is small
        elif user_guess < number_to_be_guessed:
            print(f'Try Again! You guessed too small')
# 3- if the guess is high      
        else:
            print(f' Try Again! You guessed too high')


        user_guess = int(input('try a nother one, what is your guess? '))

 

# when the number of play is over
    if run > 5:
    
        print(f'{name}, Sorry \n <<< Game is over, Good luck next time , the guessed number is {number_to_be_guessed}  >>>')
    
else:
    print('Waiting to see you again, have a nice day')