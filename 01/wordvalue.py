from data import DICTIONARY, LETTER_SCORES

def load_words():
    with open(DICTIONARY, 'r', encoding = 'utf-8') as dict_file:
        list_of_words = [word[:len(word)-1] for word in dict_file]
    """Load dictionary into a list and return list"""
    #use generator
    return list_of_words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word = word
    current_value = 0
    for letter in word:
        if letter.isalpha():
            current_value += LETTER_SCORES[letter.upper()]
        #except KeyError:pass
    return current_value

def max_word_value(word_list = None):
    current_word = None
    if word_list: current_word = __max_word_value(word_list)
    else: current_word = __max_word_value(load_words())
    return current_word
        
def __max_word_value(word_list):
    current_max_word = 0
    current_word = None
    for word in word_list:
            if current_max_word < calc_word_value(word):
                current_max_word = calc_word_value(word)
                current_word = word
    return current_word
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

if __name__ == "__main__":
    pass
    #pass # run unittests to validate
