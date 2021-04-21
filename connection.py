import sqlite3
from sqlite3 import Connection


def get_connection() -> Connection:
    try:
        return sqlite3.connect('sql.db')
    except Exception as e:
        print(e)
    return None
