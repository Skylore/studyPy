import time


def timer(n=5,k=0.5):
    def write():
        nonlocal n
        nonlocal k
        # while n >= 0:
        print(n, end = ' ')
        n = n-1
        time.sleep(k)
    return write

t = timer(5,1)
t()
t()
t()
t()
t()
t()


print('')


def timerr (n = 0, k = 0):
    def tiiime():
        for i in range(n, -1, -1):
            yield i
    v = tiiime()
    for j in v:
        time.sleep(k)
        print(j, end = ' ')


timerr(5, 3)