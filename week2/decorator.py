from datetime import datetime


def gettime(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        res = func(*args, **kwargs)
        print(datetime.now() - start)

        return res
    return wrapper


@gettime
def one(n):
    l = []

    for i in range(10 ** n):
        if i % 2 == 0:
            l.append(i)

    return l


@gettime
def two(n):
    # start = datetime.now()
    l = [i for i in range(10 ** n) if i % 2 == 0]
    # print(datetime.now() - start)

    return l


g = gettime(one)(5)


print(g)
