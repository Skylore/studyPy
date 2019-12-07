class Car:
    cars = 0
    #
    # def __init__(self, color):
    #     self.color = 'red'
    #     self.speed = 20
    #     Car.cars += 1

    @classmethod
    def print_chars(cls):
        # print(cls.cars)
        my_car = super(Car, cls).__new__(cls)
        my_car.color = 'black'
        my_car.__init__()
        return my_car

    @staticmethod
    def info(self):
        print(self.color)

    # def __str__(self):
    #     return self.color

#
# car = Car()
# car1 = Car()
# car2 = Car()
#
# Car.info(car1)


car = Car.print_chars()
print(car)
