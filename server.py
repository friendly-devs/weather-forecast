import socket
import re
import mysql.connector
import threading

from connection import get_connection
from utils import str_to_bytes, bytes_to_str
from constants import SERVER_HOST, SERVER_PORT, SERVER_DATA_LENGTH, MESSAGE_SUCCESS
from user import UserManager
from weather import WeatherManager


class HandleClient:
    def __init__(self, client_socket: socket, connect: mysql.connector.CMySQLConnection):
        self.client = client_socket
        self.userManager = UserManager(connect)
        self.weatherManager = WeatherManager(connect)
        self.is_login = False
        self.is_admin = False

    def start(self):
        try:
            while True:
                data: bytes = self.client.recv(SERVER_DATA_LENGTH)
                data: str = bytes_to_str(data)
                data: str = data.strip()

                # break
                if data.startswith('exit'):
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

        if self.userManager.login(username, password):
            self.client.sendall(MESSAGE_SUCCESS)
            self.is_login = True
            if username == 'admin':
                self.is_admin = True
        else:
            self.client.sendall(b'Username hoac mat khau bi sai')

    def register(seft, data: str):
        items = data.split(' ')
        _, username, password = items

        pattern = '[a-zA-Z0-9]{2,64}'

        if re.match(pattern, username) and re.match(pattern, password):
            if seft.userManager.register(username, password):
                seft.client.sendall(b'Dang ki thanh cong')
            else:
                seft.client.sendall(b'Username da ton tai')
        else:
            seft.client.sendall(b'Username va mat khau phai co 2 ki tu va nam trong [a-zA-Z0-9]')

    def find_city(self, data: str):
        if not self.is_login:
            self.client.sendall(b'Ban phai dang nhap')
            return

        items = data.split(' ')
        try:
            city_id = int(items[1])
            data = self.weatherManager.get_city(city_id)
            data = str_to_bytes(data)
            self.client.sendall(data)
        except ValueError:
            self.client.sendall(b'Du lieu khong hop le')

    def find_cities(self):
        if not self.is_login:
            self.client.sendall(b'Ban phai dang nhap')
            return

        data = self.weatherManager.get_cities()
        data = str_to_bytes(data)
        self.client.sendall(data)

    def add_city(self, data: str):
        if not self.is_admin:
            self.client.sendall(b'Ban khong co quyen admin')
            return

    def update_weather(self, data: str):
        if not self.is_login:
            self.client.sendall(b'Ban phai dang nhap')
            return


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
            handler = HandleClient(client, mysql_connect)

            thread = threading.Thread(target=handler.start, daemon=True)
            thread.start()
    except Exception as e:
        print(e)
    finally:
        mysql_connect.close()
        server.close()
