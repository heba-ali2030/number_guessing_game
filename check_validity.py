

# def user_guess():
#     user_guess= int(input('what is your guess: '))
#     if True:
#         pass
#     else:
#         print('please enter a valid number to continue! ')

# user_guess()


# def check_user_guess(user_guess):
#     try:
#         number = int(user_guess)
#         print(number)
#     except ValueError:
#         try:
#             number = float(user_guess)
#             print(number)
#         except ValueError:
#             print('please enter a valid number to continue! ')

# user_guess= int(input('what is your guess: '))

# check_user_guess(user_guess)
  

def user_guess():
    while True:
        user_guess= input('what is your guess: ')
        try:
            number = int(user_guess)
            break
        except ValueError:
            try:
               float(user_guess)
               break
            except ValueError:
                print('please enter a valid number to continue! ')

user_guess()








    
