import socket

HOST = '127.0.0.1'
PORT = 8080
DATA_LENGTH = 1024
SUCCESS = b'success'


def str_to_bytes(data: str):
    return data.encode()


def bytes_to_str(data: bytes):
    return data.decode()


def login(client):
    username = input('Nhap username: ').strip()
    password = input('Nhap password: ').strip()
    data = 'login {} {}'.format(username, password)

    client.sendall(str_to_bytes(data))
    data = client.recv(DATA_LENGTH)
    print(data)


def register(client):
    print('register')
    username = input('Nhap username: ').strip()
    password = input('Nhap password: ').strip()
    data = 'register {} {}'.format(username, password)

    client.sendall(str_to_bytes(data))
    data = client.recv(DATA_LENGTH)
    data = bytes_to_str(data)
    print(data)


def handle(client):
    while True:
        print('1. Dang nhap')
        print('2. Dang ki')
        print('3. Thoat')
        choice = input('Moi ban lua chon: ')

        if choice == '1':
            login(client)
        elif choice == '2':
            register(client)
        elif choice == '3':
            return
        else:
            print('Ban nhap khong hop le')
            continue


if __name__ == '__main__':
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        handle(client)
    finally:
        client.close()
