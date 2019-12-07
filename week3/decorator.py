def decorator(arg):
    def func_wrapper(func):
        def func_arg_wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            res.append(arg)
            return res

        return func_arg_wrapper
    return func_wrapper


@decorator(24)
def some_func(a, b, c):
    return [a + 1, b + 5, c + 2]

@decorator(10)
def another_func(a, b, c):
    return [a, b, c]


# print(some_func(1, 2, 3))
print(another_func(1, 2, 3))

#
# def one():
#     arr = (1, 2, 4)
#     (a, b, c) = *arr






