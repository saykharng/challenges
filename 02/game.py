#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random as rd
import csv
import pdb

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7
draw = ''

def draw_letters():
    draw = [chr(rd.randint(65,90)) for i in range(NUM_LETTERS)]
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    return draw


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    #pdb.set_trace()
    player1 = input('Enter a word: ')
    player1.upper()
    if not _validation(player1, draw):
        raise ValueError('Try again!')
    return player1


def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    #pdb.set_trace()
    valid_word = all([letter.upper() in draw for letter in word])
    word_is_in_dict = False
    if word.upper() in word_in_dict:
        for letter in word.upper():
            if word.count(letter) != draw.count(letter):
                break
        else:
            word_is_in_dict = True
    if valid_word and word_is_in_dict: return True
    else:raise ValueError
        
    
# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)
# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    all_possib_words = []
    for e_list in _get_permutations_draw(draw):
        if ''.join(e_list).upper() in word_in_dict:                
            all_possib_words.append(''.join(e_list).upper())
    return all_possib_words

def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    all_permutation = []
    for i in range(1, NUM_LETTERS+1):
        all_permutation.append(list(itertools.permutations(draw, i)))
    perm_flat_list = []
    for item in all_permutation:
        for word in item:
            perm_flat_list.append(word)
    return perm_flat_list

# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))

word_in_dict = {}
with open('dictionary.txt', 'r') as dict_file:
    list_for_dict = csv.reader(dict_file)
    for words in list_for_dict :
        word_in_dict[''.join(words).upper()] = calc_word_value(words)


if __name__ == "__main__":
    main()
