def razdelitel(arg):
    def omegalul(func):
        def roflanebalo(a):
            if a % arg == 0:
                return (a // arg)
            return (a)
        return roflanebalo
    return omegalul

@razdelitel(2)
def some_func(a):
    return a
print(some_func(2))