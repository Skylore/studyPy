import random


class Car:
    def __str__(self):
        return "don't use print!!!"

    def __eq__(self, other):
        print("don't use == ")
        return False


class Bmw(Car):
    count = 0

    def __init__(self):
        Bmw.count += 1


class Audi(Car):
    count = 0

    def __init__(self):
        Audi.count += 1


class Lexus(Car):
    count = 0

    def __init__(self):
        Lexus.count += 1


class Mazda(Car):
    count = 0

    def __init__(self):
        Mazda.count += 1


class Infinity(Car):
    count = 0

    def __init__(self):
        Infinity.count += 1


keys = {1: Bmw, 2: Audi, 3: Lexus, 4: Mazda, 5: Infinity}


def generate_car_set():
    return [keys[random.randint(1, 5)]() for _ in range(random.randint(5, 15))]


def get_two_cars(cars):
    return cars[random.randint(0, len(cars)) - 1], cars[random.randint(0, len(cars) - 1)]


def get_car():
    return repr(keys[random.randint(1, 5)]())
