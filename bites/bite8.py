"""
Write a function that rotates characters in a string, in both directions:

if n is positive move characters from beginning to end, e.g.: rotate('hello', 2) would return llohe
if n is negative move characters to the start of the string, e.g.: rotate('hello', -2) would return lohel
See tests for more info. Have fun!
"""

word = "hello"
#word = "bob and julian love pybites!"
#word = 'pybites loves julian and bob!'
def rotate(string, n):

        return string[n:]+string[:n]

print(rotate(word,-2))