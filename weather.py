import mysql.connector


class WeatherManager:
    def __init__(self, connect: mysql.connector.CMySQLConnection):
        self.connect = connect

    # success
    def add_city(self, name) -> bool:
        cursor = self.connect.cursor(buffered=True)
        query = """insert into cities(name) values(%s)"""
        cursor.execute(query, (name,))

        # commit data
        try:
            self.connect.commit()
            return True
        except Exception as e:
            print(e)
            return False

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
        cursor = self.connect.cursor(buffered=True)
        query = """
            select cities.id, cities.name, day, status, temp_min, temp_max from cities
            inner join weathers
            on cities.id = weathers.city_id
            where city_id={} and day between curdate() and curdate() + 6
            order by day;
        """.format(city_id)

        row_count = cursor.execute(query)

        if row_count == 0:
            return 'Chua co du lieu thoi tiet cho 7 ngay toi'
        else:
            return self.__format_data(cursor)

    # success
    def get_cities(self) -> str:
        cursor = self.connect.cursor()
        query = """
            select cities.id, cities.name, day, status, temp_min, temp_max from cities
            inner join weathers
            on cities.id = weathers.city_id
            where day=CURDATE();
        """

        row_count = cursor.execute(query)

        if row_count == 0:
            return 'Chua co du lieu thoi tiet cho hom nay'
        else:
            return self.__format_data(cursor)

    # success
    def save_weather(self, city_id: int, day: str, status: str, temp_min: int, temp_max: int) -> str:
        cursor = self.connect.cursor(buffered=True)
        query = """select count(*) from weathers where city_id={} and day='{}'""".format(city_id, day)

        cursor.execute(query)
        data = cursor.fetchone()
        count = data[0]

        if count == 0:
            return self.__add_weather(city_id, day, status, temp_min, temp_max)
        else:
            return self.__update_weather(city_id, day, status, temp_min, temp_max)

    # success
    def __update_weather(self, city_id: int, day: str, status: str, temp_min: int, temp_max: int) -> bool:
        cursor = self.connect.cursor(buffered=True)
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
        cursor = self.connect.cursor(buffered=True)
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
