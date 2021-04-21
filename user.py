from sqlite3 import Connection


class UserManager:
    def __init__(self, connect: Connection):
        self.connect = connect

    # success
    def login(self, username: str, password: str) -> bool:
        cursor = self.connect.cursor()
        query = """select username, password from users where username=?"""

        cursor.execute(query, (username,))

        for row in cursor:
            if row[1] == password:
                return True
        return False

    # success
    def register(self, username: str, password: str) -> bool:
        cursor = self.connect.cursor()
        query = """insert into users(username, password) values(?, ?)"""

        try:
            cursor.execute(query, (username, password))
            self.connect.commit()
            return True
        except Exception as e:
            print(e)
            return False
