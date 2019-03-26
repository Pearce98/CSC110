#
# Pearce Phanawong
# shaper.py
# Description: This program will print out three different shapes based
#              on user input and print out one of three shapes. This
#              program will make use of functions in order to reduce
#              redundancies with the code.
#
from os import _exit as exit

def line(number):
    '''
    This function will determine the number of rows that the shape will
    have and prints it.
    '''
    while number > 0:
        print('|---------|')
        number -= 1

def up(letter):
    '''
    This funciton will print out an upward pointing arrow using a character
    from user input.
    '''
    i = 5
    j = 0
    while i >= 0:
        print(i * ' ' + letter + j * letter)
        j += 2
        i -= 1

def down(letter):
    '''
    This function will print out a downward pointing arrow using
    a character from user input.
    '''
    i = 0
    j = 10
    while j >= 0:
        print(i * ' ' + letter + j * letter)
        j -= 2
        i += 1

def main():
    shape = input('Enter shape to display:\n')
    character = str(input('Enter arrow character:\n'))
    rows = int(input('Enter row-area height:\n'))
    print()
    if shape == 'house':
        up(character)
        line(rows)
    elif shape == 'plumbbob':
        up(character)
        line(rows)
        down(character)
    elif shape == 'hourglass':
        line(rows)
        down(character)
        up(character)
        line(rows)
    else:
        print('Invalid shape')
        exit(0)

main()