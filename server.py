import socket
import re
import mysql.connector
import threading

from connection import get_connection
from utils import str_to_bytes, bytes_to_str
from constants import SERVER_HOST, SERVER_PORT, SERVER_DATA_LENGTH
from user import UserManager


class HandleClient:
    def __init__(self, client: socket, connect: mysql.connector.CMySQLConnection):
        self.client: socket = client
        self.userManager = UserManager(connect)
        self.is_login = False
        self.is_admin = False

    def start(self):
        try:
            while True:
                data: bytes = self.client.recv(SERVER_DATA_LENGTH)
                data: str = bytes_to_str(data)
                data: str = data.strip()

                # break
                if len(data) == 0 or data.startswith('exit'):
                    break

                print(data)

                if data.startswith('login'):
                    self.login(data)
                elif data.startswith('register'):
                    self.register(data)
                elif data.startswith('cities'):
                    self.find_cities()
                elif data.startswith('city'):
                    self.find_city(data)
                elif data.startswith('add_city'):
                    self.add_city(data)
                elif data.startswith('update_weather'):
                    self.update_weather(data)
                else:
                    self.client.sendall(b'Command khong hop le')

        except Exception as e:
            print(e)
        finally:
            self.client.close()

    def login(self, data: str):
        items = data.split(' ')
        _, username, password = items

        regex = ''


    def register(seft, data: str):
        print(data)

    def find_city(self, data: str):
        print(data)

    def find_cities(self):
        print('find cities')

    def add_city(self, data: str):
        print(data)

    def update_weather(self, data: str):
        print(data)


if __name__ == '__main__':
    try:
        mysql_connect = get_connection()

        if mysql_connect is None:
            print('Khong the ket noi den MYSQL')
            exit(1)

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((SERVER_HOST, SERVER_PORT))
        server.listen()

        while True:
            client, _ = server.accept()
            handler = HandleClient(client=client, connect=mysql_connect)

            thread = threading.Thread(target=handler.start, daemon=True)
            thread.start()
    except (KeyboardInterrupt, SystemExit):
        print('Shutdown server')
        client.close()
        server.close()
