import random
names = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']
#Can you write a simple list comprehension to convert these names to title case (brad pitt -> Brad Pitt).
# Or reverse the first and last name?

new_list = [ name.title() for name in names ]
print(new_list)

reverse_list = [ i.split()[1].title()+ " "+i.split()[0].title() for i in names]
print(reverse_list)

#Then use this same list and make a little generator, for example to randomly return a pair of names, try to make this work:

def random_team():
    firstnames = [name.split()[0] for name in names]
    for i in firstnames:
        yield random.choice(i)



#         yield random.choice(i)
#
gen = random_team()
print(next(gen))
# print(next(gen))