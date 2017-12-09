from data import DICTIONARY, LETTER_SCORES
filename = 'dictionary.txt'

def load_words():
    with open(filename, 'r', encoding = 'utf-8') as name_file:
        list_of_words = [word for word in name_file]
    """Load dictionary into a list and return list"""
    return list_of_words

def calc_word_value():
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    pass

def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    pass

if __name__ == "__main__":
    pass # run unittests to validate
