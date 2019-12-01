def add(*args):
    res = 0

    for i in args:
        res += i

    return res


# print(add(1, 2, 3, 2, 1, 2, 4, 5, 1, 2, 5, 6))


def one(**kwargs):
    for i in kwargs:
        print(kwargs[i], end = ' ')


# 1 2 3

one()


def mult(a, b=5):
    return a * b

#
# print(mult(10))
# mult(4)
# mult(5)
# mult(19)
# print(mult(4, 3))


def sumTwo(a: float, b: float):
    return a + b


sumTwo(1, 5)
sumTwo(4, 6)





