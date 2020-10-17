import db
import statements
from contacts import Contact


def menu():
    connection = db.connect()
    db.create_tables(connection)

    while (option := input(statements.MENU_PROMPT)) != '4':
        if option == '1':
            name = input("What is the name of the contact? ")
            number = input("What is the phone number of the contact? ")

            db.add(connection, name, number)

            print("New contact added to list.")
        elif option == '2':
            for name, number in db.get_all(connection):
                contact = Contact(name, number)
                print(contact.details())
        elif option == '3':
            name = input("What is the name of the contact? ")
            (contact_name, contact_number) = db.get_by_name(connection, name)
            contact = Contact(contact_name, contact_number)
            print(contact.details())


if __name__ == '__main__':
    menu()
