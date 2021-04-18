import mysql.connector
from constants import MYSQL_HOST, MYSQL_PORT, MYSQL_DB, MYSQL_USERNAME, MYSQL_PASSWORD


def get_connection() -> mysql.connector.CMySQLConnection:
    try:
        return mysql.connector.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            database=MYSQL_DB,
            user=MYSQL_USERNAME,
            password=MYSQL_PASSWORD
        )
    except Exception as e:
        print(e)
        return None

#
# cursor = connect.cursor()
#
# query = """insert into users(username, password) values(%s, %s)"""
#
# cursor.execute(query, ('user0143', '7789'))
# connect.commit()
#
# query = """select username, password from users"""

# cursor.execute(query)
#
# for (username, password) in cursor:
#     print(username, password)
#
# cursor.close()
# connect.close()
