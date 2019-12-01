def one():
    x = ['1', '2']

    def stats():
        print(x)
        print(id(x))

    stats()

    return stats


class One:
    def __init__(self):
        self.x = ['1', '2']

    def stats(self):
        print(self.x)
        print(id(self.x))
