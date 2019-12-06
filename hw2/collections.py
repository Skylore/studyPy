# TODO  дан словарь json и путь path в формате root>child>0>... где child это имя дочернего элемента, а 0 индекс обьекта
#  root>child>0>...   ->    {"root": {"child": ['...']}}
#  метод parse_path должен пройти по пути path в словаре json и вернуть полученное значение


def parse_path(json, path):
    path = path.split('>')
    for i in path:
        if i in '0123456789':
            json = json[int(i)]
        else:
            json = json[i]
    return json



# TODO метод tuple_of_primes должен создать кортеж состоящий из простых чисел не превышающих n
#  Использовать генераторы списков


def tuple_of_primes(n):
    least = []
    k = 0
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                k = k + 1
        if k == 0:
            least.append(i)
        else:
            k = 0
    return tuple(least)

# TODO метод delete_repetition принимает некоторое количество массивов и должен соеденить массивы в один
#  где будут содержатся числа без повторений


def delete_repetition(*args):
    res = []
    for i in args:
        res.extend(i)
    res = set(res)
    return res