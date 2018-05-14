text = 'Awesome, I am doing 100 days python'
#starts with Awesome?
print(text.startswith('Awesome'))
#ends with python?
print(text.endswith('python'))
#replace 100 wth 200
print(text.replace('100', '200'))

import re
####regex#####
text = 'Awesome, I am doing the #100DaysOfCode challenge'

print(re.search(r'I am', text))

print(re.match(r'I am', text))
print(re.match(r'Awesome.*challenge',text))

hundred = 'Awesome, I am doing the #100DaysOfCode challenge'
two_hundred = 'Awesome, I am doing the #200DaysOfCode challenge'

m = re.search(r'(#\d+DaysOfCode)', hundred)
ma = re.match(r'.*(#\d+DaysOfCode).*', hundred)

print(m.group())
print(ma)

###findall
text = '''
$ python module_index.py |grep ^re
re                 | stdlib | 005, 007, 009, 015, 021, 022, 068, 080, 081, 086, 095
'''

print(re.findall(r'\d+',text))

text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum"""

print(re.findall(r'\w+',text))
from collections import Counter
cnt = Counter(re.findall(f'[A-Z][a-z-9]+', text))
print(cnt.most_common(5))
print(re.findall(f'[A-Z][a-z-9]+', text))

#print(text.split()[:5])

movies = '''1. Citizen Kane (1941)
2. The Godfather (1972)
3. Casablanca (1942)
4. Raging Bull (1980)
5. Singin' in the Rain (1952)
6. Gone with the Wind (1939)
7. Lawrence of Arabia (1962)
8. Schindler's List (1993)
9. Vertigo (1958)
10. The Wizard of Oz (1939)'''.split('\n')
print(movies)
#print(re.search(r'\w+',movies))



####sub
text = '''Awesome, I am doing #100DaysOfCode, #200DaysOfDjango and of course #365DaysOfPyBites'''
print(re.sub(r'\d+','100',text))
print(re.sub(r'(#\d+DaysOf)\w+',r'\1Python',text))