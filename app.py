import statements
import db as database
from contacts import Contact


def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (option := input(statements.MENU_PROMPT)) != '4':
        if option == '1':
            add_new_contact(connection)
        elif option == '2':
            show_all_contacts(connection)
        elif option == '3':
            show_requested_contact(connection)


def add_new_contact(connection):
    name = input("What is the name of the contact? ")
    number = input("What is the phone number of the contact? ")
    database.add(connection, name, number)

    print("New contact added to list.")


def show_all_contacts(connection):
    for id, name, number in database.get_all(connection):
        contact = Contact(name, number)
        print(contact.details())


def show_requested_contact(connection):
    (name, number) = database.get_by_name(
        connection, input("What is the name of the contact? ")
    )
    contact = Contact(name, number)
    print(contact.details())


if __name__ == '__main__':
    menu()
