from collections import Counter
import calendar
import itertools
import random
import re
import string
import requests

names = ' pybites mike bob julian tim sara guido'.split()
print(names)

for name in names:
    print(name.title())

first_half_alphabet = list(string.ascii_lowercase)[:13]
print(first_half_alphabet)

new_name = []

for i in names:
    if i[0] in first_half_alphabet:
        new_name.append(i.title())
print(new_name)

m = [name.title() for name in names if name[0] in first_half_alphabet
     ]
print(m)

request = requests.get('http://projects.bobbelderbos.com/pcc/harry.txt')
words = request.text.lower().split()
print(words[:5])

cnt = Counter(words)
print(cnt.most_common(5))

words = [re.sub(r'\W+', r'', word) for word in words]
print("-" in words)

resp = requests.get("http://projects.bobbelderbos.com/pcc/stopwords.txt")
stopwords = resp.text.lower().split()
print(stopwords[:5])

words = [ word for word in words if word.strip() and word not in stopwords]
print(words)
cnt1 = Counter(words)
print(cnt1.most_common(5))
