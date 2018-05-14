from functools import wraps
import time

def mydecorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        #do something before the origina function called
        #call the passed in function
        result = function(*args, **kwargs)
        #do something after the original function
        return result
    #return wrapper = decorated function
    return wrapper

@mydecorator
def my_function(args):
    pass

my_function = mydecorator(my_function)

def show_args(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print('hi from decorator - args:')
        print(args)
        result = function(*args, *kwargs)
        print('hi again from decorator - kwargs:')
        print(kwargs)
        return result
    return wrapper

@show_args
def get_profile(name, active=True, *sports, **kwargs):
    print('\n\thi from the get_profile functions\n')

get_profile('bob', True, 'basketball', 'soccer', pythonista='special honor', topcoder='2017 code winner')