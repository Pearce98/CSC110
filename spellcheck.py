#
# Pearce Phanawong
# spellcheck.py
# Description: This program takes in a file called misspellings.txt
#              and creates a dictionary with it. The dictionary is used
#              to replace the words in a file the user inputs. It then
#              either replaces the words that are misspelled and prints
#              that out, or suggests how to change the spelling of words
#              in the file.
#
#

def main():
    dictionary = create_dictionary()

    misspellings = input('Enter input file:\n')
    misspellings_list = open(misspellings, 'r').readlines()

    #ms is short for misspellings
    ms_list = []
    for i in range(len(misspellings_list)):
        ms_list.append(misspellings_list[i].strip('\n'))

    mode = input('Enter spellcheck mode (replace or suggest):\n')
    print()
    print('--- OUTPUT ---')

    if mode == 'suggest':
        suggest_mode(ms_list, dictionary)
    elif mode == 'replace':
        replace_mode(ms_list, dictionary)

def create_dictionary():
    '''
    This function opens misspellings.txt and populates a dictionary
    with misspelled words and the values of the misspelled words
    being the correctly spelled version of those words. The function
    will return the dictionary.
    '''
    text = open('misspellings.txt', 'r').readlines()
    list_of_lines = []
    for i in range(len(text)):
        list_of_lines.append(text[i].strip('\n'))
    dictionary = {}
    key_list = []
    value_list = []
    for i in range(len(list_of_lines)):
        split_list = list_of_lines[i].split(':')
        value_list.append(split_list[0])
        key_list.append(split_list[1])
    for i in range(len(key_list)):
        temp_list_key = key_list[i].split(',')
        temp_list_value = value_list[i]
        for i in range(len(temp_list_key)):
            dictionary[temp_list_key[i]] = temp_list_value
    return dictionary

def replace_mode(ms_list, dictionary):
    '''
    This function will replace the misspelled words from the
    input file and will replace them with the correctly
    spelled words from the dictionary, and print it.
    '''
    for i in range(len(ms_list)):
        split = ms_list[i].split(' ')
        for word in range(len(split)):
            if split[word].lower() in dictionary:
                last = split[word][len(split[word])-1]
                first_letter = split[word][0]
                split[word] = change_lower(split[word])
                split[word] = dictionary[split[word]]
                if first_letter.isupper():
                    split[word] = change_upper(split[word])
                    print(split[word], end=' ')
                else:
                    print(split[word], end=' ')
            else:
                print(split[word], end=' ')
        print()

def suggest_mode(ms_list, dictionary):
    '''
    This function will suggest a replacement to misspelled
    words inside of the input file. It will first print the
    misspelled file and the legend after it with the suggested
    replacements.
    '''
    number_of_misspellings = 1
    legend = []
    first_letter_list = []
    for i in range(len(ms_list)):
        split = ms_list[i].split(' ')
        for word in range(len(split)):
            if split[word].lower() in dictionary:
                print(split[word], '(' + str(number_of_misspellings) + ')' , end=' ')
                legend.append(dictionary[split[word].lower()])
                number_of_misspellings += 1
                first_letter_list.append(split[word][0])
            else:
                print(split[word], end=' ')
        print()
    print()
    print('--- LEGEND ---')
    for i in range(len(legend)):
        if first_letter_list[i].isupper():
            legend[i] = change_upper(legend[i])
            print('(' + str(i+1) + ') ' + legend[i])
        else:
            print('(' + str(i+1) + ') ' + legend[i])

def change_lower(word):
    '''
    Returns a word with the first letter now being lowercase
    '''
    word = word.split()
    word[0] = word[0].lower()
    word = ''.join(word)
    return word

def change_upper(word):
    '''
    Returns a word with the first letter now being uppercase
    '''
    word = word.split()
    word[0] = word[0].capitalize()
    word = ''.join(word)
    return word

main()