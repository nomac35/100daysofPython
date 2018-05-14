import random
import itertools
names = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

def gen_pairs():
    first_names = [name.split()[0].title() for name in names]

    while True:

        first, second = None,None
        while first == second:
            first,second = random.sample(first_names,2)

        yield "{} teams up with {}".format(first,second)

gen = gen_pairs()

for _ in range(5):
    print(next(gen))


itertools.islice(gen,10)

print(list(itertools.islice(gen,10)))
