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
