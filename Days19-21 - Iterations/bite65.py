"""
This Bite focusses on the use of itertools. To that extend you complete get_possible_dict_words and _get_permutations_draw to get all valid dictionary words for a random draw of 7 letters.

This is fed into the tests that calculate the word with maximum value (work previously done for Bite 3) and there you go: you have a Scrabble cheat tool (Scrabble fans, pay attention or maybe skip this Bite!).

For example a draw of letters G, A, R, Y, T, E, V would give highest valued word GARVEY (13 points).


"""
import itertools
import os
import urllib.request
import random
import string
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}

dictionary = os.path.join(os.path.dirname(__file__), 'dictionary.txt')
#urllib.request.urlretrieve("https://raw.githubusercontent.com/pybites/challenges/master/01/dictionary.txt", dictionary)
#DICTIONARY = os.path.join('/tmp', 'dictionary.txt')

with open(dictionary) as f:
    dict= set([word.strip().lower() for word in f.read().split()])
print(dict)

alphabet = list(string.ascii_lowercase)
draw = random.choices(alphabet,k=7)


def _get_permutations_draw(draw):
    words = []
    for i in range(1,8):
        for p in itertools.permutations(draw,i):
            words.append(p)
    return words

print(_get_permutations_draw(draw))


def get_possible_dict_words(draw):
     score = {}
     p = _get_permutations_draw(draw)
     for i in p:
         #print("".join(list(i)).lower())
         if ("".join(i).lower()) in dict:
             for n in i:
                 total = 0
                 for n in i:
                    total += LETTER_SCORES[n.upper()]
                    score["".join(i).lower()]=total
     print(score)
     sn = max(score, key = score.get)
     num = score[sn]
     result = [k for k, v in score.items() if v == num]
     return tuple(result)


