import time
def timer (sec = 0, liz = 0,):
    def vremia():
        for i in range(sec, -1, -1):
            yield i
    nety = vremia()
    for j in nety:
        time.sleep(liz)
        print(j)

timer(5, 3)

