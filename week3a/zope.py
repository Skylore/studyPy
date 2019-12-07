import zope.interface
from zope.interface import implementer


class IShop(zope.interface.Interface):
    products = zope.interface.Attribute("""products list""")

    def print_products(self):
        """print products list"""


@implementer(IShop)
class Nike:
    def __init__(self, prod_list):
        self.prod_list = prod_list

    def print_products(self):
        print(self.prod_list)


nike = Nike([1, 2, 3, 4, 5])
nike.print_products()
