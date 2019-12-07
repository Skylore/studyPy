class Test:
    # def __init__(self):
    #     print('initialized')

    def __new__(cls, *args, **kwargs):
        print('created')


Test()
