#In the first while loop, we ask the user for their age and store their
# input in age. If age is a valid (decimal) value, 
# we break out of this first while
# loop and move on to the second, 
# which asks for a password. Otherwise, we
# inform the user that they need to enter a number and again ask them to
# Manipulating Strings 131
# enter their age. In the second while loop, we ask for a password, store the
# user’s input in password, and break out of the loop if the input was alphanumeric. If it wasn’t, we’re not satisfied so we tell the user the password needs
# to be alphanumeric and again ask them to enter a password.
# #

while True:
    print("Enter you age:")
    age=input()
    if age.isdecimal():
        break
    print('Please enter a number for you age.')
    
    while True:
        print('Select a new password( letters and numbers only):')
        password=input()
        if password.isalnum():
            break
        print('Password can only have letters and numbers')