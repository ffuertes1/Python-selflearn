#This is a guees the number game

import random

secretNumber=random.randint(1,20)
print('I am thinking of a number between 1 and 20')

#Ask the player to guess 6 times

for guessesTaken in range(1,7):
    print('Take a guess')
    guess=int(input())
    
    if guess<secretNumber:
        print ('your guess is too low.')
    elif guess> secretNumber:
        print('The guess number is too high')
    else:
        break # this condition is the correct guess
    
if guess== secretNumber:
    print('Good job! You guessed the number in ' + str(guessesTaken) + 'guesses!')
else:
    print ('nope. The number I was thinking ' +str(secretNumber))