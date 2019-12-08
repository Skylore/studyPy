class ContactList:
    contacts = []

    def __init__(self, contacts=None):
        if contacts is None:
            contacts = []

        ContactList.contacts = contacts