# inner nested

#nested


def one():
    x = 10

    def nested(x):
        return x + 10

    x = nested(x)
    x = nested(x)
    x = nested(x)

    print(x)


def two():
    x = 10

    def inner():
        nonlocal x
        x += 10

    inner()
    inner()
    inner()

    print(x)
