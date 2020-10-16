from db import DatabaseManager


def start_app():
    if view_contacts():
        db = DatabaseManager()

        return db.all()

    return add_contact()


def view_contacts():
    view = input('Would you like to view your contacts list? (y/n) ')

    return True if view == 'y' else False


def add_contact():
    name = input('What is the name of the contact? ')
    number = input('What is the phone number of the contact? ')

    db = DatabaseManager()
    db.create(name, number)

    return db.get(name)


def run_db_checks():
    db = DatabaseManager()
    db.check_db()


if __name__ == '__main__':
    run_db_checks()

    print(start_app())

