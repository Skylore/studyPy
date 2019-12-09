class User:
    def __init__(self, name, password, age):
        self.__name = name
        self.__password = password
        self.__age = age

    def __str__(self):
        return ("Avtoryfdnjfdsfsi {}".format(self.name))

    def __lt__(self, other):
        return self.age < other.age

    def getname(self):
        return self.name

    def getpass(self):
        return self.password

    def getage(self):
        return self.age

    def setname(self, name):
        self.name = name

    def setpassword(self, password):
        self.password = password

    def setnage(self, age):
        self.age = age

    def __eq__(self):
        return self.name == other.name
User1 = User("ROFLANOLEG", "hochyebatsia", 20)
User2 = User("OMEGAVANIA", 1232, 13)
print(User1)
print(User1 > User2)
#User3

#User4

