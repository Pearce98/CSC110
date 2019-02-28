#
# Pearce Phanawong
# avatar.py
# Description: This program creates an avatar, and the code makes use of various
#              function. The program has three preset avatars and also has an
#              option to create a custom avatar, which will ask the user several
#              questions based to determine how the avatar will look. The
#              program uses a function to print each "chunk" of the avatar's
#              body.
#

def main():
    print('----- AVATAR -----')
    i = 0
    while i < 1:
        type = input('Select an Avatar or create your own:\n')
        if type == 'exit':
            return
        elif type == 'Jeff':
            jeff()
            i += 1
        elif type == 'Adam':
            adam()
            i += 1
        elif type == 'Chris':
            chris()
            i += 1
        elif type == 'custom':
            custom()
            i += 1



def jeff():
    '''
    This function will print out a preset avatar of Jeff.
    '''
    hat('both')
    face('True', '0')
    arms('=')
    torso(2)
    legs(2, '#HHH#')

def adam():
    '''
    This function will print out a preset avatar of Adam.
    '''
    hat('right')
    face('False', '*')
    torso(1)
    arms('T')
    torso(3)
    legs(3, '<|||>')

def chris():
    '''
    This function will print out a preset avatar of Chris.
    '''
    hat('front')
    face('True', 'U')
    torso(1)
    arms('W')
    torso(1)
    legs(4, '<>-<>')

def custom():
    '''
    This function will print out a custom avatar based on user
    inputs. It will prompt the user to input several
    characteristics which will determine the look of the avatar.
    '''
    print('Answer the following questions to create a custom avatar')
    #These inputs will be the variable passed into the functions
    side = input('Hat style ?\n')
    eye = input('Character for eyes ?\n')
    shag = input('Shaggy hair (True/False) ?\n')
    strength = input('Arm style ?\n')
    top = int(input('Torso length ?\n'))
    bottom = int(input('Leg length (1-4) ?\n'))
    kicks = input('Shoe look ?\n')
    hat(side)
    face(shag, eye)
    arms(strength)
    torso(top)
    legs(bottom, kicks)


def hat(side):
    '''
    This function will print out the avatar's hat. The direction
    the hat is facing is based on user input, whether it is
    pointed to the left, right, both sides, or in the front.
    '''
    print()
    print('       ~-~')
    print('     /-~-~-\\')
    if side == 'left':
        print(' ___/_______\\')
    elif side == 'right':
        print('    /_______\\___')
    elif side == 'both':
        print(' ___/_______\\___')
    else:
        print('    /_______\\')


def face(hair, eyes):
    '''
    This function will print out the avatar's face. The hair changes
    based on user input whether it is shaggy or not, and the eyes
    are characters based on user input.
    '''
    if hair == 'True':
        print('    |"""""""|')
    elif hair == 'False':
        print("    |'''''''|")
    print('    | ' + eyes + '   ' + eyes + ' |')
    print('    |   V   |')
    print('    |  ~~~  |')
    print('     \_____/')


def arms(muscle):
    '''
    This function will print out the avatar's arms as well as one
    row of it's torso. The function takes input and will change
    the character of the arm to the input.
    '''
    print(' ' + '0', end = '')
    i = 4
    while i > 0:
        print(muscle, end = '')
        i -= 1
    print('|---|', end = '')
    i = 4
    while i > 0:
        print(muscle, end = '')
        i -= 1
    print('0')


def torso(height):
    '''
    This function will print out the avatar's torso. The length of
    the torso will change based on the variable passed into the
    function.
    '''
    while height > 0:
        print('      |-X-|')
        height -= 1


def legs(length,shoe):
    '''
    This function will print out the avatars legs and feet. The
    height of the legs will change based on user input. The style
    of the shoe will also be the shape of a 5 character string
    the user inputs.
    '''
    print('      HHHHH')
    a = 0
    b = 5
    while length > 0:
        i = b
        while i > 0:
            print(' ', end = '')
            i -= 1
        print('/// ', end = '')
        j = a
        while j > 0:
            print('  ', end = '')
            j -= 1
        print('\\\\\\')
        a += 1
        b -= 1
        length -= 1
    print(shoe + '       ' + shoe)

main()