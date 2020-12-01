import random, sys, os

def nofile():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\nThe file containing the english words could not be located.')
    print('Please make sure you downloaded and placed the file in the same directory as that of the script.')
    print('Please see the github for more details.\n\n\n')
    sys.exit(1)


def word_finder_func(len_of_word):


    try:
        fh = open('words.txt')
        number_of_words = 0

        for i in fh:
            number_of_words += 1

        fh.close()
        fh1 = open('words.txt')
    except:

        nofile()
    counter = 0

    final_word = None

    word_list = []

    for word in fh1:
        counter += 1
        if len(word.strip()) == len_of_word:
            word_list.append(word.rstrip())


    final_word = word_list[(random.randint(0,len(word_list)))]
    
    return final_word