def counter():
    x = 1

    def incrementer():
        nonlocal x
        print(x)
        x += 1

    return incrementer


c = counter()

c()
c()
c()
c()
c()

