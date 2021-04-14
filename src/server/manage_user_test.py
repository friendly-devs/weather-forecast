import unittest
from manage_user import UserIO, UserManager
from user import User


class MyTestCase(unittest.TestCase):
    def test_read_user(self):
        # Arrange
        file_name = 'users.test.txt'
        data = 'admin 123456\n' + 'user 123\n'

        with open(file_name, 'w') as file:
            file.write(data)

        expected = [User('admin', '123456'), User('user', '123')]

        # Act
        users = UserIO.read_users(file_name)

        # Assert
        self.assertEqual(expected, users)

    def test_write_user(self):
        # Arrange
        file_name = 'users.test.txt'
        expected = 'user 123\n' + 'admin 123456\n'

        # Act
        UserIO.save_users(file_name, [User('user', '123'), User('admin', '123456')])

        text = ''
        with open(file_name, 'r') as file:
            for line in file.readlines():
                text += line

        # Assert
        self.assertEqual(expected, text)


class UserManagerTest(unittest.TestCase):
    def test_login(self):
        # Arrange
        file_name = 'users.test.txt'
        username = 'admin'
        password = '123456'

        # Act
        userManager = UserManager(file_name)

        # Assert
        self.assertEqual(True, userManager.login(username, password))

    def test_register(self):
        # Arrange
        username = 'newUsername'
        password = 'newPassword'
        file_name = 'users.test.txt'

        # Act
        userManager = UserManager(file_name)

        # Assert
        self.assertEqual(True, userManager.register(username, password))
        self.assertEqual(False, userManager.register(username, password))


if __name__ == '__main__':
    unittest.main()
