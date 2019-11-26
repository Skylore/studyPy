import unittest
from hw1 import main
from hw1 import utils


class TestUtilsMethods(unittest.TestCase):

    def test_count_cars(self):
        self.assertEqual(main.count_cars(), {'bmw': utils.Bmw.count, 'audi': utils.Audi.count,
                                             'lexus': utils.Lexus.count, 'mazda': utils.Mazda.count,
                                             'infinity': utils.Infinity.count})

    def test_cars_equals(self):
        self.assertEqual(main.is_equals(), repr(main.car1) == repr(main.car2))

    def test_create_instance(self):
        self.assertEqual(main.create_instance(), main.random_car)


if __name__ == '__main__':
    unittest.main()
