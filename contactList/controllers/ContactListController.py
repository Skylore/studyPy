from contactList.models import Contact, ContactList

class ContactListController:
    @staticmethod
    def add_contact(name, surname, phone, email=None):
        ContactList.ContactList.contacts.append(Contact.Contact(name, surname, phone, email))

    @staticmethod
    def find_contact(**kwargs):
        for c in ContactList.ContactList.contacts:
            try:

                for arg_name in kwargs:
                    if getattr(c, 'get_{}'.format(arg_name))() != kwargs[arg_name]:
                        raise ValueError
                return c
            except ValueError:
                continue

    @staticmethod
    def remove_contact(phone):
        for c in ContactList.ContactList.contacts:
            if c.get_phone() == phone:
                ContactList.ContactList.contacts.remove(c)
                return c

    @staticmethod
    def all():
        print("\n".join(str(i) for i in ContactList.ContactList.contacts))

    @staticmethod
    def info():
        print('in contact list {} contacts'.format(len(ContactList.ContactList.contacts)))
