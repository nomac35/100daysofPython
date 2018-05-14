def greet(fn):
    def wrapper(*args, **kwargs):
        return "Welcome "+fn(*args)
    return wrapper

@greet
def names(name):
    return name

print(names("Alper"))



def p_decor(function):
    def wrapper(*args):
        return "<p>{}</p>".format(function(*args))
    return wrapper

@p_decor
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)


print(get_text("Alper"))

total = 0

for i in range(1,5):
    total+=i
    #print(total)

def added():
    print(sum([i for i in range(1,5)]))
added()

a ={1,2,3,4,5}
b={3,4,5,6,7,8}

print(set(a&b))
print(set(a | b))
