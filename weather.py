from sqlite3 import Connection


class WeatherManager:
    def __init__(self, connect: Connection):
        self.connect = connect

    # success
    def add_city(self, name) -> bool:
        cursor = self.connect.cursor()
        query = """insert into cities(name) values(?)"""

        # commit data
        try:
            cursor.execute(query, (name,))
            self.connect.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def list_city(self):
        cursor = self.connect.cursor()
        query = """select id, name from cities"""
        cursor.execute(query)
        rows = cursor.fetchall()

        if len(rows) == 0:
            return 'Khong co thanh pho de show'

        result = '{:10s} {:20s}\n'.format('Id', 'Ten thanh pho')
        for (id, name) in rows:
            result += '{:10s} {:20s}\n'.format(str(id), name)
        return result

    # success
    def __format_data(self, rows) -> str:
        result = '{:10s} {:20s} {:20s} {:20s} {:20s} {:20s}\n'.format(
            'City_id',
            'Ten thanh pho',
            'Thoi gian',
            'Trang thai',
            'Nhiet do thap',
            'Nhiet do cao'
        )

        for (city_id, name, day, status, temp_min, temp_max) in rows:
            result += '{:10s} {:20s} {:20s} {:20s} {:20s} {:20s}\n'.format(
                str(city_id),
                name,
                str(day),
                status,
                str(temp_min),
                str(temp_max)
            )
        return result

    # success
    def get_city(self, city_id) -> str:
        cursor = self.connect.cursor()
        query = """
            select cities.id, cities.name, day, status, temp_min, temp_max from cities
            inner join weathers
            on cities.id = weathers.city_id
            where city_id={} and day between date() and date('now', '+6 day')
            order by day;
        """.format(city_id)

        cursor.execute(query)
        rows = cursor.fetchall()

        if len(rows) == 0:
            return 'Chua co du lieu thoi tiet cho 7 ngay toi'
        else:
            return self.__format_data(rows)

    # success
    def get_cities(self) -> str:
        cursor = self.connect.cursor()
        query = """
            select cities.id, cities.name, day, status, temp_min, temp_max from cities
            inner join weathers
            on cities.id = weathers.city_id
            where day=date();
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        if len(rows) == 0:
            return 'Chua co du lieu thoi tiet cho hom nay'
        else:
            return self.__format_data(rows)

    # success
    def save_weather(self, city_id: int, day: str, status: str, temp_min: int, temp_max: int) -> str:
        cursor = self.connect.cursor()
        query = """select count(*) from weathers where city_id={} and day='{}'""".format(city_id, day)

        try:
            cursor.execute(query)
            data = cursor.fetchone()
            count = data[0]
        except Exception as e:
            print(e)
            return False

        if count == 0:
            return self.__add_weather(city_id, day, status, temp_min, temp_max)
        else:
            return self.__update_weather(city_id, day, status, temp_min, temp_max)

    # success
    def __update_weather(self, city_id: int, day: str, status: str, temp_min: int, temp_max: int) -> bool:
        cursor = self.connect.cursor()
        query = """
            update weathers 
            set 
                status='{}',
                temp_min={},
                temp_max={}
            where city_id={} and day='{}'
        """.format(status, temp_min, temp_max, city_id, day)

        try:
            cursor.execute(query)
            self.connect.commit()
            return True
        except Exception as e:
            print(e)
        return False

    # success
    def __add_weather(self, city_id: int, day: str, status: str, temp_min: int, temp_max: int) -> bool:
        cursor = self.connect.cursor()
        query = """
            insert into weathers(city_id, status, day, temp_min, temp_max)
            values({}, '{}', '{}', {}, {})
        """.format(city_id, status, day, temp_min, temp_max)

        try:
            cursor.execute(query)
            self.connect.commit()
            return True
        except Exception as e:
            print(e)
        return False
