class ContactList:
    def __init__(self, contacts=None):
        if contacts is None:
            contacts = []
        self.contacts = contacts


class Contact:
    def __init__(self, name, surname, email, phone):
        pass

    # getters

    # setters

    # __str__

    # __eq__  (phone)

    # __lt__ (first name char)


class ContactListController:
    def __init__(self, contact_list):
        self.contact_list = contact_list

    # TODO
    # add_contact, remove_contact,
    # find_contact(**kwargs)   name=Max
    # __str__
    # info       count

    pass

if __name__ == '__main__':
    controller = ContactListController(None)

    while True:
        command = input()

        #  add Max Max Max@Max 095Max

        # remove name Max



        # controller.add()