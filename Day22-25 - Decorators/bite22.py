from functools import wraps


def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
def hello():
    return "hello world"

print(hello())  ## returns "<b><i>hello world</i></b>"

from functools import wraps

def make_html(element):
    def wraped(fn):
        @wraps(fn)
        def wrapper():
            return "<{}>".format(element) + fn() + "</{}>".format(element)
        return wrapper
    return wraped

@make_html("p")
@make_html("Strong")
def get_text(text="i code with Pybites"):
    return text


print(get_text())