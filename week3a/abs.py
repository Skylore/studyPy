from abc import ABCMeta, abstractmethod, abstractproperty, ABC


class Shop:
    __metaclass_ = ABCMeta

    @abstractmethod
    def print_products(self):
        """print all products"""

    @abstractproperty
    def products(self):
        """product list """


class Nike(Shop):
    def __init__(self):
        self._products = []

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, products):
        self._products = products

    def print_products(self):
        print(self._products)


nike = Nike()

nike.products = [1, 2, 3, 4, 5]
print(nike.products)
