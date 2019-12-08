class Contact:
    pass


class ContactList:
    contacts = []

    def __init__(self, contacts=None):
        if contacts is None:
            contacts = []

        ContactList.contacts = contacts


class ContactListController:
    pass


#    run
if __name__ == '__main__':
    pass