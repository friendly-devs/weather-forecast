class Weather:
    def __init__(self, id, name, weather, min, max):
        self.id = id
        self.name = name
        self.weather = weather
        self.min = min
        self.max = max

    def __eq__(self, other):
        if not isinstance(other, Weather):
            return NotImplemented
        return self.id == other.id and \
               self.name == other.name and \
               self.min == other.min and \
               self.max == other.max and \
               self.weather == other.weather

    def __str__(self):
        return "{} {} {} {} {}".format(self.id, self.name, self.weather, self.min, self.max)
