# TODO  дан словарь json и путь path в формате root>child>0>... где child это имя дочернего элемента, а 0 индекс обьекта
#  root>child>0>...   ->    {"root": {"child": ['...']}}
#  метод parse_path должен пройти по пути path в словаре json и вернуть полученное значение


def parse_path(json, path):
    path = path.split('>')
    current = None

    for i in range(len(path)):
        try:
            path[i] = int(path[i])
        except ValueError:
            pass

    for i in path:
        current = json[i] if current is None else current[i]

    return current
    pass


# TODO метод tuple_of_primes должен создать кортеж состоящий из простых чисел не превышающих n
#  Использовать генераторы списков

def tuple_of_primes(n):
    return (i for i in range(n) if is_prime(i))
    pass


def is_prime(n):
    for i in range(1, n + 1):
        if i != 1 and i != n and n % i == 0:
            return False
    return True
    pass


# TODO метод delete_repetition принимает некоторое количество массивов и должен соеденить массивы в один
#  где будут содержатся числа без повторений

def delete_repetition(*args):
    res = set()

    for i in args:
        for j in i:
            res.add(j)

    return list(res)
