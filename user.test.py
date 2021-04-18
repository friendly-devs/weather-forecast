import unittest
import uuid
from connection import get_connection
from user import UserManager


class MyTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(MyTestCase, self).__init__(*args, **kwargs)
        self.init_data()

    def init_data(self):
        connect = get_connection()
        self.manager = UserManager(connect)

    def test_login_user(self):
        # Act
        result = self.manager.login('admin', '123456')

        # Assert
        self.assertEqual(True, result)

    def test_register_user(self):
        # Arrange
        username = str(uuid.uuid4())

        # Act
        expected_to_true = self.manager.register(username, '123456')
        expected_to_false = self.manager.register(username, '123456')

        # Assert
        self.assertEqual(True, expected_to_true)
        self.assertEqual(False, expected_to_false)


if __name__ == '__main__':
    unittest.main()
