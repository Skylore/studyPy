from contactList.controllers import ContactListController as controller

if __name__ == '__main__':
    controller.ContactListController()

    controller.ContactListController.add_contact('Ivan', 'Turchin', 'my_mail', '0952690000')
    controller.ContactListController.add_contact('Vova', 'Stich', 'vova_mail', '2345690000')
    controller.ContactListController.add_contact('Sanya', 'Gabko', 'sanyo_mail', '32452690000')

    contact = controller.ContactListController.find_contact(surname='Gabko')

    controller.ContactListController.remove_contact('0952690000')

    controller.ContactListController.all()

    controller.ContactListController.info()
