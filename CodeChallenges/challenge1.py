import os
DICTIONARY = os.path.join(os.path.dirname(__file__),'dictionary.txt')
print(DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]

LETTER_SCORES = { }
for i in scrabble_scores:
    print(i)
    for b in i[1]:
        LETTER_SCORES[b] = i[0]
print(LETTER_SCORES)


def load_words():
    with open(DICTIONARY, 'r') as f:
        return [i.strip() for i in f.read().split()]

print(load_words())
def calc_word_value():
    return sum([ LETTER_SCORES.get(char.upper(), 0)for char in word])


def max_word_value():
    if words is None:
        words = load_words()
    return max(words, key=calc_word_value)

if __name__ == "__main__":
    pass  # run unittests to validate
