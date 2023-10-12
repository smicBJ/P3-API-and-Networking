
total_run_count = 0


def my_decorator_func(func):

    def wrapper_function():
        global total_run_count
        func()
        total_run_count += 1
        print("The first decorator was run")

    return wrapper_function


def my_second_decorator_func(func):

    def wrapper_function():
        # first they get request
        # Info from it
        # Middleware
        func()
        # convert data
        # respond to the user
        print("The second decorator was run")

    return wrapper_function


@my_decorator_func
@my_second_decorator_func
def email_student():
    print("Student was emailed!")


# students = ["hudson", "nolan", "ethan", "jack", "leo"]

for _ in range(5):
    email_student()

print(total_run_count)
