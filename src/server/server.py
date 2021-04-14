import socket
import re
from manage_user import UserManager

HOST = '127.0.0.1'
PORT = 8080
DATA_LENGTH = 1024
SUCCESS = b'success'

file_name = 'users.txt'
userManager = UserManager(file_name)


def bytes_to_str(data):
    if isinstance(data, bytes):
        return data.decode()
    return None


def check_login(data):
    items = data.split(' ')

    if len(items) != 3:
        return False

    return userManager.login(items[1], items[2])


def login(client, data):
    if not check_login(data):
        client.sendall(b'Username hoac password sai')
    else:
        client.sendall(SUCCESS)
        while True:
            data = client.recv(DATA_LENGTH)
            data = bytes_to_str(data)

            print(data)

            if data.startswith('exit'):
                raise Exception('Client exit')


def register(client, data):
    items = data.split(' ')

    _, username, password = items
    regex = '^[a-zA-Z0-9]{4,}$'

    if re.match(regex, username) and re.match(regex, password):
        if userManager.register(username, password):
            client.sendall(b'Dang ki thanh cong')
        else:
            client.sendall(b'Username da ton tai')
    else:
        client.sendall(b'Username va password can co do dai la 4, chi chua cac ki tu (a-zA-Z0-9)')


def handle_client(client):
    try:
        while True:
            data = client.recv(DATA_LENGTH)
            data = bytes_to_str(data)

            print(data)

            if data.startswith('login'):
                login(client, data)

            elif data.startswith('register'):
                register(client, data)

            elif data.startswith('exit'):
                break

            else:
                client.sendall(b'Sai command')
    finally:
        client.close()


if __name__ == '__main__':
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen()

        while True:
            connect, _ = server.accept()
            handle_client(connect)
    finally:
        server.close()
