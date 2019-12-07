class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def print_color(self):
        print(self.color)

    def move(self):
        print('sdfihsfilushdifuhshf')

    def info(self):
        print('color =', self.color, 'speed =', self.speed)

car1 = Car('red', 100)
car2 = Car('black', 200)

# car1.print_color()
# car2.print_color()
#
# car1.info()
# car2.info()  # color = red   speed = 100


print(car1.color)
print(car1.speed)
