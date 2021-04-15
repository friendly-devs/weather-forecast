from weather import Weather


class WeatherIO:
    @staticmethod
    def read_weathers(file_name):
        weathers = []

        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                item = line.strip().split(', ')
                if len(item) == 5:
                    weathers.append(Weather(item[0], item[1], item[2], item[3], item[4]))

        return weathers


class WeatherManager:
    def __init__(self, file_name):
        self.weathers = WeatherIO.read_weathers(file_name)

    def get_all(self):
        result = ''
        for weather in self.weathers:
            result += '\n' + weather.__str__()
        return result.strip()

    def get_by_id(self, id):
        for weather in self.weathers:
            if weather.id == id:
                return weather.__str__()

        return None
