class User(object):
    def __init__(self, name, password, age):
        self.__name = name
        self.__password = password
        self.__age = age

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def __str__(self):
        return 'name: {}, age: {}'.format(self.__name, self.__age)

    def __eq__(self, other):
        return self.__name == other.getName()


user = User('2', 'wfs', 25)
print(user)

user1 = User('1', 'sdf', 25)

print(user == user1)