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
