import re
from user import User


class UserIO:

    @staticmethod
    def read_users(file_name):
        users = []

        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                items = line.strip().split(' ')
                if len(items) == 2:
                    user = User(items[0], items[1])
                    users.append(user)

        return users

    @staticmethod
    def save_users(file_name, users):
        with open(file_name, 'w') as file:
            for user in users:
                file.write("{} {}\n".format(user.username, user.password))


class UserManager:
    def __init__(self, file_name):
        self.dict = {}
        users = UserIO.read_users(file_name)
        for user in users:
            self.dict[user.username] = user

    def login(self, username, password):
        user = self.dict.get(username)
        if user is not None:
            return user.password == password
        return False

    def register(self, username, password):
        if self.dict.get(username) is not None:
            return False

        regex = '^[a-zA-Z0-9]{4,}$'

        if re.match(regex, username) and re.match(regex, password):
            self.dict[username] = User(username, password)
            return True

        return False
