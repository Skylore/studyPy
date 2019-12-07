# def car(x=0, y=0):
#
#     def move(dx, dy):
#         nonlocal x
#         nonlocal y
#
#         x += dx
#         y += dy
#
#         print('{} {}'.format(x, y))
#
#     def absolute():
#         print((x ** 2 + y ** 2) ** 0.5)
#
#     return {'move': move, 'absolute': absolute}
#
#
# v = car(3, 4)
#
# v['move'](1, 2)
# v['move'](1, 1)
# v['move'](1, 1)
#
# v['absolute']()
#
#
# class Car:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self, dx, dy):
#         self.x += dx
#         self.y += dy
#
#         print('{} {}'.format(self.x, self.y))
#
#     def absolute(self):
#         print((self.x ** 2 + self.y ** 2) ** 0.5)
#
#
# v = Car(3, 4)
#
# v.move(1, 2)
# v.move(1, 1)
# v.move(1, 1)
#
# v.absolute()
#
#
