import random

# __ private      _ protected


class Car:
    def __init__(self, color, speed, name):
        self.__color = color
        self.__speed = speed
        self.__name = name
        self._clss = 'Car'

    def getColor(self):
        return self.__color

    def getSpeed(self):
        return self.__speed

    def setColor(self, color):
        self.__color = color

    def setSpeed(self, speed):
        self.__speed = speed

    def move(self, distance):
        print('moved to: ', distance / self.__speed, 's')

    def __str__(self):
        return 'color: {}, speed: {}, name: {}'.format(self.__color, self.__speed, self.__name)


# Car - superclass

class Bmw(Car, object):
    def __init__(self, color, speed, name):
        super().__init__(color, speed, name)

    # Overriding
    def __str__(self):
        return '12345676'

    def print_clss(self):
        return self._clss


class Mercedes(Car):
    def __init__(self, color, speed, name):
        super().__init__(color, speed, name)


class Audi(Car):
    def __init__(self, color, speed, name):
        super().__init__(color, speed, name)


def keyFactory():
    colors = ('red', 'yellow', 'black')
    speed = (24, 50, 30)

    return colors[random.randint(0, 2)], speed[random.randint(0, 2)]


bmw = Bmw(*keyFactory(), 'bmw')
audi = Audi(*keyFactory(), 'audi')
mb = Mercedes(*keyFactory(), 'mb')

print(bmw)
print(audi)
print(mb)


print(bmw.print_clss())


