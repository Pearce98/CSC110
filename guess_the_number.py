#
# Pearce Phanawong
# guess_the_number.py
# Description: This program will ask the user to input a number, then
#              ask again for another number. If the second is the
#              same as the first, the user wins. The user has two
#              attempts, and if both are failed, the user loses.
#
from os import _exit as exit

n = input('Enter number to be guessed between 10 and 100, inclusive:\n')
if n.isnumeric() == True:
    n = int(n)
else:
    print(n,'is not 10-100, inclusive.')
    exit(0)
if n < 10 or n > 100:
    print(n,'is not 10-100, inclusive.')
    exit(0)
guess1 = input('First guess:\n')
if guess1.isnumeric() == False:
    print('Guess is invalid.')
    exit(0)
else:
    guess1 = int(guess1)
if guess1 == n:
    print(guess1, 'is correct! Ending game.')
elif guess1 != n:
    print(guess1, 'is incorrect.')
    guess2 = input('Second guess:\n')
    if guess2.isnumeric() == False:
        print('Guess is invalid.')
        exit(0)
    else:
        guess2 = int(guess2)
    if guess2 == n:
        print(guess2, 'is correct! Ending game.')
    elif guess2 != n:
        print(guess2, 'is incorrect.')
        print('You did not guess the number within 2 attempts.')
        print('The target number was', n)
        print('Your guesses were', guess1, 'and', guess2)