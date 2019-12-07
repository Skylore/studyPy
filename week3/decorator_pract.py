def divider(func):
    def wrapper(a, b):
        print(a, b)

    return wrapper


@divider
def some_func(a, b):
    return '12345'


some_func(1, 2)