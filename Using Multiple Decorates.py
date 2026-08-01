def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

def add_greeting(func):
    def wrapper():
        return "Hello " + func()
    return wrapper

def add_ending(func):
    def wrapper():
        return func() + ", have a good day!"
    return wrapper


@uppercase
@add_ending
@add_greeting
def get_name():
    return "Tobias"


print(get_name())
