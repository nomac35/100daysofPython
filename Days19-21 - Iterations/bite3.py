"""
Calculate the dictionary word that would have the most value in Scrabble.

There are 3 tasks to complete for this Bite:

First write a function to read in dictionary.txt (DICTIONARY constant) and return a list of words.
Second write a function that receives a word and calculates its value. Use the scores stored in LETTER_SCORES.
With these two pieces in place, write a third function that takes a list of words and returns the word with the highest value.
Look at the TESTS tab to see what your code needs to pass. Enjoy!
"""

import os
import urllib.request

import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


# START HERE
def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY) as f:
        return [word.strip() for word in f.read().split()]


def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)

def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    if words is None:
        words = load_words()
    return max(words, key=calc_word_value)