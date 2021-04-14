class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return "[username: {}, password: {}]".format(self.username, self.password)

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented

        return self.username == other.username and self.password == other.password