#
# Pearce Phanawong
# tower_bridge.py
# Description: This program will print out an ASCII style
#              image of the Tower Bridge in London. The
#              user will be asked to input 4 different
#              numbers to make it vary in size.
#

bl = int(input('enter bridge length:\n'))
lth = int(input('lower tower height length:\n'))
uth = int(input('upper tower height length:\n'))
tw = int(input('enter tower width:\n'))

print('    +  ' + ' ' * tw + '  +  ' + ' ' * bl + '  +  ' + ' ' * tw + '  +')
print(('    |||' + '^' * tw + 'uu|  ' + ' ' * bl + '  |uu' + '^' * tw + '|||' +'\n') * uth, end = '')
print('     \\u' + '^' * tw + 'u/===' + '=' * bl + '===\\u' + '^' * tw + 'u/')
print(('     |u' + '.' * tw + 'u|   ' + ' ' * bl + '   |u' + '.' * tw + 'u| ' + '\n') * lth, end = '')
print('_____|u' + '.' * tw + 'u|___' + '_' * bl + '___|u' + '.' * tw + 'u|_____')
print('====HHH' + 'H' * tw + 'HH===' + '=' * bl + '===HH' + 'H' * tw + 'HHH====')
print(('    HHH' + 'H' * tw + 'HH   ' + ' ' * bl + '   HH' + 'H' * tw + 'HHH    ' + '\n')* 3)