import sqlite3

class DatabaseManager:
    def __init__(self, database='contacts.db'):
        self.database = database


    def make_connection(self):
        self.connection = sqlite3.connect(self.database)

        return self.connection.cursor()


    def check_db(self):
        cursor = self.make_connection()

        cursor.execute("""CREATE TABLE IF NOT EXISTS contacts (
            name text,
            number integer
        )""")

        self.connection.commit()

        self.connection.close()


    def all(self):
        cursor = self.make_connection()

        cursor.execute("SELECT * FROM contacts")

        result = cursor.fetchall()

        self.connection.commit()

        self.connection.close()

        return result;


    def get(self, name):
        cursor = self.make_connection()

        cursor.execute("SELECT * FROM contacts WHERE name = ?", (name,))

        result = cursor.fetchone()

        self.connection.commit()

        self.connection.close()

        return result;


    def create(self, name, number):
        cursor = self.make_connection()

        cursor.execute("INSERT INTO contacts VALUES (?, ?)", (name, number))

        self.connection.commit()

        self.connection.close()
