class Shop:
    __count = 0

    def __init__(self, name):
        Shop.__count += 1
        self.__name = name

    def print_name(self):
        print(self.__name)

    @staticmethod
    def get_count():
        print(Shop.__count)


shop1 = Shop('adidas')
shop2 = Shop('nike')

# shop1.print_name()
# shop2.print_name()

Shop.print_name(shop2)
