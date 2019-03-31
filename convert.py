#
# Pearce Phanawong
# convert.py
# Description: This program makes use of a dictionary. It reads a file
#              and produces a dictionary of foreign words with their
#              matching English translation. It asks the user for a word
#              and if it is in the dictionary, it will print the English
#              translation, and if not, it will print "Not sure."
#

def get_word_conversions(words_file_name):
    '''
    This function returns a dictionary of foreign words with their
    values being the English version of the word.
    '''
    text = open(words_file_name, 'r').readlines()
    list_of_words = []
    for i in range(len(text)):
        list_of_words.append(text[i].strip('\n'))
    convert = {}
    for i in range(len(list_of_words)):
        split_list = list_of_words[i].split(',')
        for j in range(len(split_list)-1):
            convert[split_list[j+1]] = split_list[0]
    return convert

def print_conversion(word, conversions):
    '''
    This function prints out the word's English version if the word
    passed into the function is in the dictionary. If the word is
    not in the dictionary, it will print "Not sure."
    '''
    print()
    if word in conversions:
        print('English version is:', conversions[word])
    else:
        print('Not sure.')

def main():
    file_name = input('Enter name of words file:\n')
    conversions = get_word_conversions(file_name)

    word = input('Enter word to convert to English:\n')
    print_conversion(word, conversions)

main()