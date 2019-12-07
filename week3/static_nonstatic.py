class Car:
    # static var
    count = 0

    @staticmethod
    def create(color, speed):
        return Car(color, speed)

    @staticmethod
    def print_info(self):
        print(self.__color)

    # Object / nonstatic  methods
    def __init__(self, color, speed):
        self.__color = color
        self.__speed = speed
        Car.count += 1

    def getColor(self):
        return self.__color

    def getSpeed(self):
        return self.__speed

    def setColor(self, color):
        self.__color = color

    def setSpeed(self, speed):
        self.__speed = speed
    #
    # def getCount(self):
    #     return count

    def __str__(self):
        return 'color: {}, speed: {}'.format(self.__color, self.__speed)


car1 = Car('red', 4)
car2 = Car('black', 6)
car3 = Car('yellow', 9)

car3.getColor()
Car.print_info(car3)

# print(Car.count)
#
# created_car = Car.create('sfs', 35)
#
# print(created_car)
