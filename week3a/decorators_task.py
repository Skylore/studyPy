# def divider(arg):
#     def arg_wrapper(func):
#         def wrapper(a):
#             if a % arg == 0:
#                 return func(a // arg)
#             else:
#                 return func(a)
#         return wrapper
#     return arg_wrapper
#
#
# @divider(10)
# def some_func(a):
#     return a
#
#
# print(some_func(10))
# print(some_func(20))
# print(some_func(30))
#
#


