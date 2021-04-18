import unittest
from connection import get_connection
from weather import WeatherManager


class MyTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(MyTestCase, self).__init__(*args, **kwargs)
        self.init_data()

    def init_data(self):
        self.connect = get_connection()
        self.manager = WeatherManager(self.connect)

    def add_city(self):
        # Arrange
        city_name = 'name'

        # Act
        result = self.manager.add_city(city_name)

        # Assert
        self.assertEqual(True, result)

    def test_update_weather(self):
        data = self.manager.get_city(1)
        print(data)


if __name__ == '__main__':
    unittest.main()
