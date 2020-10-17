import sqlite3
import statements


def connect():
    return sqlite3.connect('contacts.db')


def create_tables(connection):
    with connection:
        connection.execute(statements.CREATE_TABLES)


def add(connection, name, number):
    with connection:
        connection.execute(statements.INSERT_ITEM, (name, number))


def get_all(connection):
    with connection:
        return connection.execute(statements.GET_ALL_ITEMS).fetchall()


def get_by_name(connection, name):
    with connection:
        return connection.execute(statements.GET_ITEMS_BY_NAME, (name, )).fetchone()
