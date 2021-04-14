import unittest
from weather import Weather
from weather_manage import WeatherIO


class MyTestCase(unittest.TestCase):
    def test_read_weathers(self):
        # Arranger
        file_name = 'weather.txt'
        expected = [Weather('1', 'Ha Noi', 'Mua', '30', '35'), Weather('2', 'HCM', 'Nang', '28', '33')]

        # Act
        result = WeatherIO.read_weathers(file_name)

        # Assert
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
