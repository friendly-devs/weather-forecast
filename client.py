import socket
from constants import SERVER_HOST, SERVER_PORT, SERVER_DATA_LENGTH

SUCCESS = 'success'


def str_to_bytes(data: str):
    return data.encode()


def bytes_to_str(data: bytes):
    return data.decode()


def login(client):
    username = input('Nhap username: ').strip()
    password = input('Nhap password: ').strip()
    data = 'login {} {}'.format(username, password)

    client.sendall(str_to_bytes(data))
    data = client.recv(SERVER_DATA_LENGTH)
    data = bytes_to_str(data)

    if data != SUCCESS:
        print(data)
        return

    client.sendall(b'cities')
    data = client.recv(SERVER_DATA_LENGTH)
    data = bytes_to_str(data)

    print('----------------------------------')
    print('Danh sach thoi thiet cac thanh pho')
    print(data)

    while True:
        text = input('Nhap id thanh pho ban muon tham khao (exit de ket thuc): ').strip()

        if text.startswith('exit'):
            client.sendall(b'exit')
            raise Exception('Client exit')

        client.sendall(str_to_bytes('city ' + text))

        data = client.recv(SERVER_DATA_LENGTH)
        data = bytes_to_str(data)
        print(data)


# success
def register(client):
    username = input('Nhap username: ').strip()
    password = input('Nhap password: ').strip()
    data = 'register {} {}'.format(username, password)

    client.sendall(str_to_bytes(data))
    data = client.recv(SERVER_DATA_LENGTH)
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
            client.sendall(b'exit')
            return
        else:
            print('Ban nhap khong hop le')
            continue


if __name__ == '__main__':
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((SERVER_HOST, SERVER_PORT))
        handle(client)
    finally:
        client.close()
        exit(0)
