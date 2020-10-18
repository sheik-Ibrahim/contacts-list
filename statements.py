INSERT_ITEM = "INSERT INTO contacts (name, number) VALUES (?, ?);"
GET_ALL_ITEMS = "SELECT * FROM contacts;"
GET_ITEMS_BY_NAME = "SELECT * FROM contacts WHERE name = ?;"
CREATE_TABLES = """
CREATE TABLE IF NOT EXISTS contacts (
    id integer primary key,
    name text,
    number integer
);
"""
MENU_PROMPT = """
--- Contacts List App ---


Please choose one of these options:

1) Add new contact
2) View all contacts
3) Find a contact by name
4) Exit


Your selection:
"""