import subprocess
import socket
import threading
from Bots.utils.Encrypt import encrypt

encrypted_password = encrypt('TROMPITA')


def launch_admin_panel():
    subprocess.run("./admin_panel.c")


def main():
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_socket.bind(('localhost', 12010))

    launcher = threading.Thread(target=launch_admin_panel)
    launcher.start()

    new_socket.listen()
    client_socket, addr = new_socket.accept()
    password = ""

    password += new_socket.recv(1024).decode('utf-8')

    encrypted_request = encrypt(password)

    if encrypted_request == encrypted_password:
        answer = True
    else:
        answer = False

    client_socket.send(answer)
    launcher.join()


if __name__ == '__main__':
    main()
