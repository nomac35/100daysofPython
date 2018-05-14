#A generator is a function that returns an iterator.
# It generates values using the yield keyword, when called with next() (a for loop does this implicitly),
# and it raises a StopIteration exception when there are no more values to generate.



def num_gen():
    for i in range(5):
        yield(i)

gen = num_gen()

print(next(gen))
print(next(gen))
print("hello")
for i in gen:
    print(i)
#print(next(gen))

options = 'red yellow blue white black green purple'.split()
print(options)

