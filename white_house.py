#
#Pearce Phanawong
#white_house.py
#Description: This program will print out an ASCII style
#             image of the white house. The user will
#             be asked to input 3 different numbers
#             to make it vary in size.
#

side = int(input('Specify side width:\n'))
mid = int(input('Specify middle width:\n'))
flag = int(input('Specify flag height:\n'))
height = int((side+mid)/4)+1
print()
print(' ' + '   ' * side + '    ' * mid + '|##')
print((' ' + '   ' * side + '    ' * mid + '|\n') * flag, end='')
print(' ' + '   ' * side + '.-.-' * mid + '\'\''  + '-.-.' * mid)
print(' ' + '   ' * side + ';.__' * mid + '--' + '__.;' * mid)
print('.' + '___' * side + '[---' * mid + '--' + '---]' * mid + '___' * side + '.')
print(('|' + 'II ' * side + '||II' * mid + 'HH' + 'II||' * mid + ' II' * side + '|' + '\n' +
'|' + '.. ' * side + '||..' * mid + '||' + '..||' * mid + ' ..' * side + '|' + '\n') * height)