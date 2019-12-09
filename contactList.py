class ContactList:
    contacts = []
    def __init__(self, contacts=None):
        if contacts is None:
            contacts = []
        ContactList.contacts = contacts





class Contact:
    def __init__(self, name, surname, email, phone):
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__phone = phone

    def getname(self):
        return self.__name

    def getsurname(self):
        return self.__surname

    def getemail(self):
        return self.__email

    def getphone(self):
        return self.__phone

    def setname(self, name):
        self.__name = name

    def setsurname(self, surname):
        self.__surname = surname

    def setemail(self, email):
        self.__email = email

    def setnphone(self, phone):
        self.__phone = phone

    def __eq__(self, other):
        return self.__phone == other.getphone()

    def __lt__(self, other):
        return self.__name[0] < other.getname()

    def __str__(self):
        return "name: {}, surname: {}, email: {}, phone: {}".format(self.__name, self.__surname, self.__email, self.__phone)

class ContactListController:
    def __init__(self, contact_list):
        self.contact_list = contact_list

    @staticmethod
    def add_contact(name, surname, email, phone ):
        ContactList.contacts.append(Contact(name, surname, email, phone))


    @staticmethod
    def remove_contact(phone):
        for i in ContactList.contacts:
            if i.getphone() == phone:
                ContactList.contacts.remove(i)

    @staticmethod
    def all():
        print("/n".join(str(i) for i in ContactList.contacts ))

    @staticmethod
    def find_contact(phone):
        for i in ContactList.contacts:
            if i.getphone() == phone:
                print("vi gay")

    @staticmethod
    def info_contact():
        print(len(ContactList.contacts))
    # TODO
    # add_contact, remove_contact,
    # find_contact(**kwargs)   name=Max
    # __str__
    # info       count

    pass

if __name__ == '__main__':
    ContactList()
    ContactListController.add_contact("sasha", "gabkoooooooooooooooooo", "gabko@gabko", "095988293")
    ContactListController.all()



        #  add Max Max Max@Max 095Max

        # remove name Max



        # controller.add()