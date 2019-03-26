#
# Pearce Phanawong
# decrypter.py
# Description: This program will ask the user for the name
#              of the encrypted file and the index file. It will
#              write a new file called 'decrypted.txt' with the
#              original contents before going through the
#              encrypter.py program.
#

def main():
    encrypted_file = input('Enter the name of a mixed text file:\n')
    index_file = input('Enter the mix index file:\n')
    encrypted = open(encrypted_file, 'r').readlines()
    indexed = open(index_file, 'r').readlines()

    #This loop will make lists of the opened files
    encrypt_list = []
    index_list = []
    for i in range(len(indexed)):
        encrypt_list.append(encrypted[i].strip('\n'))
        index_list.append(int(indexed[i].strip('\n')))

    #This loop will match the correct line of the encrypted code
    #to the correct spot based on the index list
    decrypt = []
    for i in range(len(index_list)+1):
        for j in range(len(index_list)):
            if index_list[j] == i:
                decrypt.append(encrypt_list[j])

    #This will write the new decrypted file
    decrypted = open('decrypted.txt', 'w')
    for i in range(len(decrypt)):
        decrypted.write(decrypt[i] + '\n')

main()