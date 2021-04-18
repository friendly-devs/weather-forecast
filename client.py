import socket
from constants import SERVER_HOST, SERVER_PORT, SERVER_DATA_LENGTH
from utils import str_to_bytes, bytes_to_str

SUCCESS = 'success'


class HandleServer:
    def __init__(self, socket_client: socket.socket):
        self.client = socket_client
        self.is_login = False
        self.is_admin = False

    def start(self):
        while True:
            print('1. Dang nhap')
            print('2. Dang ki')
            print('3. Thoat')
            choice = input('Moi ban lua chon: ')

            if choice == '1':
                self.login()
            elif choice == '2':
                self.register()
            elif choice == '3':
                self.exit()
            else:
                print('Ban nhap khong hop le')

    def register(self):
        username = input('Nhap username: ').strip()
        password = input('Nhap password: ').strip()
        data = 'register {} {}'.format(username, password)

        self.client.sendall(str_to_bytes(data))
        data = client.recv(SERVER_DATA_LENGTH)
        data = bytes_to_str(data)
        print(data)

    def exit(self):
        self.client.close()
        exit(0)

    def login(self):
        username = input('Nhap username: ').strip()
        password = input('Nhap password: ').strip()
        data = 'login {} {}'.format(username, password)

        client.sendall(str_to_bytes(data))
        data = client.recv(SERVER_DATA_LENGTH)
        data = bytes_to_str(data)

        if data != SUCCESS:
            print(data)
            return
        elif username == 'admin':
            self.is_admin = True
        self.menu()

    def still_connected(self):
        try:
            self.client.sendall(b'ping')
            data = self.client.recv(SERVER_DATA_LENGTH)
            return len(data) != 0
        except Exception as e:
            print(e)
            return False

    def menu(self):
        while True:
            if not self.still_connected():
                print('Disconnect')
                self.client.close()
                exit(0)

            print('----------------------------------')
            print('0. Thoat chuong trinh')
            print('1. Hien thi thoi tiet tat ca thanh pho')
            print('2. Hien thi thoi tiet cua mot thanh pho')

            if self.is_admin:
                print('3. Them mot thanh pho')
                print('4. Cap nhat thong tin thoi tiet')

            number = input('Moi ban lua chon: ').strip()

            if number == '0':
                self.exit()
            elif number == '1':
                self.show_cities()
            elif number == '2':
                self.show_city()
            elif number == '3':
                self.add_city()
            elif number == '4':
                self.update_weather()
            else:
                print('Ban nhap khong hop le')

    def show_cities(self):
        self.client.sendall(b'cities')
        data = self.client.recv(SERVER_DATA_LENGTH)
        data = bytes_to_str(data)

        print('----------------------------------')
        print('Danh sach thoi tiet cac thanh pho')
        print(data)

    def show_city(self):
        while True:
            text = input('Nhap id thanh pho ban muon xem: ').strip()

            try:
                number = int(text)
            except ValueError:
                print('Ban phai nhap id')
                continue

            data = 'city {}'.format(number)
            data = str_to_bytes(data)
            self.client.sendall(data)

            data = self.client.recv(SERVER_DATA_LENGTH)
            data = bytes_to_str(data)

            print('----------------------------------')
            print('Danh sach thoi tiet cac ngay toi')
            print(data)
            break

    def add_city(self):
        if not self.is_admin:
            print('Ban nhap khong hop le')
            return

        name = input('Nhap ten thanh pho: ').strip()

        if len(name) == 0:
            print('Khong duoc de trong ten')
            return

        data = 'add_city {}'.format(name)
        data = str_to_bytes(data)
        self.client.sendall(data)

        data = self.client.recv(SERVER_DATA_LENGTH)
        data = bytes_to_str(data)
        print(data)

    def update_weather(self):
        if not self.is_admin:
            print('Ban nhap khong hop le')
            return

        self.client.sendall(b'list_city')
        data = client.recv(SERVER_DATA_LENGTH)
        data = bytes_to_str(data)
        print(data)

        dict = {}
        dict['city_id'] = input('City id: ').strip()
        dict['day'] = input('Ngay (yyyy-mm-dd): ').strip()
        dict['status'] = input('Trang thai: ').strip()
        dict['temp_min'] = input('Nhiet do thap nhat: ').strip()
        dict['temp_max'] = input('Nhiet do cao nhat: ').strip()

        data = 'update_weather {}'.format(str(dict))
        data = str_to_bytes(data)
        self.client.sendall(data)

        data = self.client.recv(SERVER_DATA_LENGTH)
        data = bytes_to_str(data)
        print(data)


if __name__ == '__main__':
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((SERVER_HOST, SERVER_PORT))

        handler = HandleServer(client)
        handler.start()
    except Exception as e:
        print(e)
    finally:
        client.close()
