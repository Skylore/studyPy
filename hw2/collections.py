# TODO  дан словарь json и путь path в формате root>child>0>... где child это имя дочернего элемента, а 0 индекс обьекта
#  root>child>0>...   ->    {"root": {"child": ['...']}}
#  метод parse_path должен пройти по пути path в словаре json и вернуть полученное значение


def parse_path(json, path):
    # print(path)
    path = path.split('>')
    # print(path)
    for i in path:
        if i in '0123456789':
            json = json[int(i)]
        else:
            json = json[i]
    # print(json)
    return json


# TODO метод tuple_of_primes должен создать кортеж состоящий из простых чисел не превышающих n
#  Использовать генераторы списков


def tuple_of_primes(n):
    def is_prime(k):
        for i in range(1, k + 1):
            if i != 1 and i != k and k % i == 0:
                return False
        return True
    res = [i for i in range(n) if is_prime(i)]
    return tuple(res)


# TODO метод delete_repetition принимает некоторое количество массивов и должен соеденить массивы в один
#  где будут содержатся числа без повторений


def delete_repetition(*args):
    res = []
    for i in args:
        res += i
    res = list(set(res))
    return res




