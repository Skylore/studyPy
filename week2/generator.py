def one():
    print('one')


def two():
    print('two')


def three():
    print('three')


def generator():
    yield one
    yield two
    yield three

iter = generator()

for i in iter:
    i()

