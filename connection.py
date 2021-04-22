import sqlite3
from sqlite3 import Connection


def get_connection() -> Connection:
    return sqlite3.connect('sql.db')
