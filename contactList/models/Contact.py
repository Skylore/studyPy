class Contact:
    def __init__(self, name, surname, email, phone):
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def __eq__(self, other):
        return self.__phone == other.get_phone()

    def __lt__(self, other):
        return self.__name[0] < other.get_name()[0]

    def __str__(self):
        return 'name: {}, surname: {}, email: {}, phone: {}'.format(self.__name, self.__surname, self.__email,
                                                                    self.__phone)
