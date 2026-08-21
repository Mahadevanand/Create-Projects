# Decorator to convert the returned text to uppercase
def uppercase(func):

    # Wrapper function that calls the original function
    # and converts its result to uppercase
    def wrapper():
        return func().upper()

    # Return the wrapper function
    return wrapper


# Decorator to add "Hello " before the returned text
def add_greeting(func):

    # Wrapper function
    def wrapper():

        # Call the original function and add "Hello " before it
        return "Hello " + func()

    # Return the wrapper function
    return wrapper


# Decorator to add an ending message
def add_ending(func):

    # Wrapper function
    def wrapper():

        # Call the original function and add the ending message
        return func() + ", have a good day!"

    # Return the wrapper function
    return wrapper


# Apply the decorators to the get_name function
@uppercase
@add_ending
@add_greeting
def get_name():

    # Return the name
    return "Tobias"


# Call the decorated function and print the result
print(get_name())
