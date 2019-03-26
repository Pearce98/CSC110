#
# Pearce Phanawong
# encrypter.py
# Description: This program will take in a .txt file name and
#              take the lines of text in it and write those lines
#              to another file called 'encrypted.txt' as well as
#              write the line numbers in corresponding oreder into
#              another file called 'index.txt'.
#
import random

def main():
    random.seed(125)
    file_name = input('Enter a name of a text file to mix:\n')
    text = open(file_name, 'r').readlines()

    #These loops will create lists of the opened file and the indices
    list_of_lines = []
    for i in range(len(text)):
        list_of_lines.append(text[i].strip('\n'))
    index_list = []
    for i in range(len(list_of_lines)):
        index_list.append(i+1)

    #This loop will swap all the indices around in the lists 5 times
    for i in range(0,5):
        for i in range(len(index_list)):
            first = random.randint(0,len(index_list)-1)
            second = random.randint(0,len(index_list)-1)
            index_list[first], index_list[second] = index_list[second], index_list[first]
            list_of_lines[first], list_of_lines[second] = list_of_lines[second], list_of_lines[first]
    encrypted = open('encrypted.txt', 'w')

    #These next lines will write the encrypted lines to the new files
    for i in range(len(list_of_lines)):
        encrypted.write(list_of_lines[i] + '\n')
    index_file = open('index.txt', 'w')
    for i in range(len(index_list)):
        index_file.write(str(index_list[i]) + '\n')


main()