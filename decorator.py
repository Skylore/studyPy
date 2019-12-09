def decorator(func):
    def wrapper(*args,**kwargs):
        print("OMEGALUL")
        return func(*args,**kwargs)
        print("ROFLANEBALO")
    return wrapper
@decorator
def some_func(a, b, c):
    return a + 1, b - 1, c - 1
print(some_func(1,2,3))