from hw1 import utils

cars = utils.generate_car_set()
car1, car2 = utils.get_two_cars(cars)
random_car = utils.get_car()

# TODO: метод count_cars должен посчитать количество машин разных моделей в массиве cars
#  и записать в соответствующие переменные


def count_cars():
    bmw = 0
    audi = 0
    lexus = 0
    mazda = 0
    infinity = 0

    for i in (cars):
        if (type(i)).__name__ is 'Bmw':
            bmw += 1
        elif (type(i)).__name__ is 'Lexus':
            lexus += 1
        elif (type(i)).__name__ is 'Audi':
            audi += 1
        elif (type(i)).__name__ is 'Mazda':
            mazda += 1
        elif (type(i)).__name__ is 'Infinity':
            infinity += 1

    return {'bmw': bmw, 'audi': audi, 'lexus': lexus, 'mazda': mazda, 'infinity': infinity}


# TODO: метод is_equals должен сравнить модель машин car1 и car2 и вернуть True или False


def is_equals():
    if (type(car1)).__name__ is (type(car2)).__name__:
        return True
    else:
        return False


# TODO: метод create_instance должен вернуть машину модели, которая записана в переменной random_car


def create_instance():
    return eval('random_car')