import unittest
from contactList.controllers import ContactListController
from contactList.models import ContactList
from contactList.models import Contact


class TestController(unittest.TestCase):
    def test_add_contact(self):
        name = 'test_name'
        surname = 'test_surname'
        email = 'test_email'
        phone = 'test_phone'

        test_contact = Contact.Contact(name, surname, email, phone)

        ContactListController.ContactListController.add_contact(test_contact.get_name(), test_contact.get_surname(), test_contact.get_email(), test_contact.get_phone())

        self.assertTrue(test_contact in ContactList.ContactList.contacts)

        ContactList.ContactList.contacts.remove(test_contact)

    def test_remove(self):
        name = 'test_name'
        surname = 'test_surname'
        email = 'test_email'
        phone = 'test_phone'

        test_contact = Contact.Contact(name, surname, email, phone)

        ContactListController.ContactListController.add_contact(name, surname, email, phone)
        ContactListController.ContactListController.remove_contact(phone)

        self.assertFalse(test_contact in ContactList.ContactList.contacts)


    # remove_contact    find_contact    info


if __name__ == '__main__':
    unittest.main()
