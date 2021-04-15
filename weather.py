class Weather:
    def __init__(self, id, name, data):
        self.id = id
        self.name = name
        self.data = data

    def get_one_day(self):
        today = self.data[0]
        status, min, max = today
        return '{id} {name:10s} {status:10s} {min} {max}'.format(id=self.id, name=self.name, status=status, min=min,
                                                                 max=max)

    def get_seven_days(self):
        text = '{}\n'.format(self.name)
        text += '----------------\n'
        for day in self.data:
            status, min, max = day
            text += '{:10s} {} {}\n'.format(status, min, max)
        return text


class WeatherIO:
    @staticmethod
    def read_weathers(file_name):
        weathers = []

        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                items = line.strip().split(', ')
                if len(items) == 23:
                    id = items[0]
                    name = items[1]
                    tmp = items[2:]

                    data = []

                    for i in range(0, 7):
                        index = i * 3
                        data.append([tmp[index], tmp[index + 1], tmp[index + 2]])

                    weather = Weather(id, name, data)
                    weathers.append(weather)

        return weathers


class WeatherManager:
    def __init__(self, file_name):
        self.weathers = WeatherIO.read_weathers(file_name)

    def get_all(self):
        result = ''
        for weather in self.weathers:
            result += weather.get_one_day() + '\n'
        return result

    def get_by_id(self, id):
        for weather in self.weathers:
            if weather.id == id:
                return weather.get_seven_days()

        return None
