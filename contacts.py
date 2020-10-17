class Contact:
    def __init__(self, name, number):
        """Create new instance of contact."""
        self.name = name
        self.number = number

    def get_name(self):
        """Get the name of the contact."""
        return self.name

    def get_number(self):
        """Get the number of the contact."""
        return self.number

    def details(self):
        """Get full details of the contact."""
        return """
        Name: {},
        Number: {}
        """.format(self.name, self.number)
