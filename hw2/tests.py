import unittest
import random
from hw2 import utils
from hw2 import collections


class TestCollections(unittest.TestCase):
    def test_parse(self):
        test_set = utils.get_path()
        json = utils.json

        self.assertEqual(id(collections.parse_path(json, test_set[0])), id(test_set[1]))

    def test_make_tuple_of_primes(self):
        def is_prime(k):
            for i in range(1, k + 1):
                if i != 1 and i != k and k % i == 0:
                    return False
            return True

        n = (0, 1, 10, 1000)
        for test_value in n:
            self.assertEqual(list(collections.tuple_of_primes(test_value)), list(i for i in range(test_value) if is_prime(i)))

    def test_delete_repetition(self):
        for i in range(10):
            test_arrs = [[random.randint(0, 100) for _ in range(random.randint(3, 20))]
                         for _ in range(random.randint(0, 10))]

            clear_arr = [set(i) for i in test_arrs]
            res = set()

            for i in clear_arr:
                res = res.union(i)

            self.assertEqual(len(set(collections.delete_repetition(*test_arrs))), len(collections.delete_repetition(*test_arrs)))
            self.assertEqual(set(collections.delete_repetition(*test_arrs)), res)


if __name__ == '__main__':
    unittest.main()