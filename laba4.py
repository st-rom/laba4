def raise_func(arg):
    if type(arg) == dict:
        raise KeyError
    if type(arg) == list:
        raise IndexError


def except_func():
    try:
        raise_func()
    except:
        print('everything is fine')


def raise_error(arg):
    if type(arg) == list:
        raise KeyError


class Raiser(Exception):
    def __init__(self):
        super().__init__('Hello')


def myexcept_raise_func():
    raise Raiser


try:
    myexcept_raise_func()
except Raiser as a:
    print(a)


