class Person:
    def __init__(self, name, email):
        self.name = str(name)
        self.email = str(email)

    def __repr__(self) -> str:
        return f"Name: {self.name}, email: {self.email}"

    def print_info(self) -> str:
        return repr(self)


