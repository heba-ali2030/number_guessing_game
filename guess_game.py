import random

# check validity of user input
# 1- check numbers
def check_validity(user_guess):
    while user_guess.isdigit() == False:
        user_guess = input('please enter a valid number to continue: ')
    return (int(user_guess))

# 2- check string
def check_name(name):
    while name.isalpha() == False:
        print('Ooh, Sorry is it your name?!')
        name = input('Please enter your name: ')
    return name

# begin the game and ask the user to press yes to continue
print(f'Are you ready to play this game : Type Yes button to begin: ')
play = input(f' Type Yes or Y to continue and Type No or N to exit \n ').lower()

if play == 'yes' or play == 'y':
    
    # get user name
    name = check_name(input('Enter your name: \n'))

    # get the number range from the user
    first = check_validity(input('enter the first number you want to play: \n first number:  '))
    last = check_validity(input('enter the last number of range you want to play: \n last number:  '))

    # tell the user that range
    print (f'Hello {name}, let\'s begin! the number lies between {first} and {last} \n You have 5 trials')

    
    number_to_be_guessed = random.randint(first, last)
    # print(number_to_be_guessed)

    # Number of times for the guess game to run
    run = 1
    while run <= 5:
    
        run += 1
        user_guess = check_validity(input('what is your guess: '))

        # if user guess is in the range
        if user_guess in range(first, last):
            print('Great beginning, you are inside the right range')

            # 1- if the user guess is true
            if user_guess == number_to_be_guessed:
                print(f'Congratulation, you got it, the number is: {number_to_be_guessed}')
                break
        
             # 2- if the guess is high 
            elif user_guess > number_to_be_guessed:
                print(f' Try Again! You guessed too high')
            
            # 3 - if the guess is small
            else:
                print(f'Try Again! You guessed too small')
        
#         # if the user guess is out of range
        else:
            print (f'You are out of the valid range, you should enter a number from {first} to {last} only!')
            

#     # when the number of play is over
    else:
        print(f'{name}, Sorry \n <<< Game is over, Good luck next time , the guessed number is {number_to_be_guessed}  >>>')

# # when user type no:
else:
    print('Waiting to see you again, have a nice day')







