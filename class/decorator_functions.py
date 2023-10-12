import time

# Decorator functions, also known as function wrappers, allow programmers to modify the behavior of
# function or class. Decorators allow us to wrap another function in order to extend the behavior of
# the wrapped function, without permanently modifying it. In Decorators, functions are taken as the
# argument into another function and then called inside the wrapper function.

total_run_count = 0


# Her we create the decorator function
def my_decorator_func(func):

    # Inside, we create a wrapper function, that calls the func passed as a paramater somehwere in side
    def wrapper_function():
        global total_run_count
        func()
        total_run_count += 1
        print("The first decorator was run")

    # At the end, we call the function
    # IMPORTANT NOTE: Notice how we do not use parenthesis when returning the function
    return wrapper_function


def my_second_decorator_func(func):

    def wrapper_function():
        func()
        print("The second decorator was run")

    return wrapper_function


# While functions can take multiple decorators, the order matters
# The close to the function definition, the sooner the decorator will be run
@my_second_decorator_func
@my_decorator_func
def email_student():
    print("Student was emailed!")


for _ in range(5):
    email_student()

print(total_run_count)


# Example with paramaters
def time_decorator(func):

    # This wrapper function gets the start time, runs the inner function, and prints out the difference
    # We use args and kwargs to make sure all the paramaters are passed
    def wrap(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(func.__name__, end - start)
        return result

    return wrap


@time_decorator
def countdown_to_run(n):
    while n > 0:
        n -= 1


countdown_to_run(5)
countdown_to_run(1000)
# This next one might take a few seconds depending on the speed of your computer
countdown_to_run(100000000)
