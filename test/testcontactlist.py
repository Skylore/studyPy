import unittest
import contactList

class MyTestCase(unittest.TestCase):
    def test_remove(self):
        name = "tesrnd"
        surname = "tsasijf"
        email = "ofdksakof"
        phone = "789879876"

        test_contact = contactList.Contact(name, surname, email, phone)
        contactList.ContactListController.add_contact(test_contact.getname(),test_contact.getsurname(), test_contact.getemail(), test_contact.getphone())
        self.assertTrue(test_contact in contactList.ContactList.contacts)




if __name__ == '__main__':
    unittest.main()
