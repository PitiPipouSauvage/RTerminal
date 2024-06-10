import mariadb
import pwinput
import socket 
import sys
from utils.Encrypt import encrypt


users = {
    encrypt('no227'): encrypt('hello')
}

def connect_to_db(server_ip: str, server_port=3306) -> mariadb.connect:
    try:
        conn = mariadb.connect(
            user="checker",
            password="checker",
            host=server_ip,
            port=server_port,
            database="admins"
        )

    except:
        raise ValueError('Incorect server ip or port.')
    
    cursor = conn.cursor()
    return cursor


def get_user(server_ip: str, username: str, password: str, server_port=3306) -> bool:
    cursor = connect_to_db(server_ip, server_port)
    cursor.execute('SELECT username, password FROM admins WHERE username=? AND password=?', (username, encrypt(password)))
    result = [(username, password) for username, password in cursor]
    if len(result) == 1:
        return True
    return False


def authenticate() -> bool:
    for attempts in range(3):
        sys.stdout.write('Enter username : ')
        sys.stdout.flush()
        for line in sys.stdin:
            username = line
            break

        username = username.split('\n')[0]

        password = pwinput.pwinput(prompt='Enter password : ')

        if get_user(sys.argv[1], username, password, server_port=int(sys.argv[2])):
            return True

        sys.stdout.write((2 - attempts)*f'You have {2 - attempts} attempts remaining \r')
        sys.stdout.write((-1 + attempts == 1)*'Either your username or your password is incorrect ')
        sys.stdout.write('\n')
        sys.stdout.flush()
    return False


def connect_to_target(target_ip, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target_ip, target_port))

    return socket


def execute_command(sock, command):
    total_sent = 0
    while total_sent < len(command):
        sent = sock.send(command.encode()[total_sent:])
        if sent == 0:
            return False 
        total_sent += sent 
    
    chunks = []
    bytes_recd = 0
    bytes_recd_prv = 0
    while bytes_recd != bytes_recd_prv or bytes_recd_prv == 0:
        chunk = sock.recv(2048)
        chunks.append(chunk)
        bytes_recd_prv = bytes_recd
        bytes_recd += len(chunk)
    
    return (b"".join(chunks)).decode('utf-8')


def main():
    isRunning = True 
    target_ip, target_port = input("Enter target ip and port as such <target_ip> <target_port> : ").split(' ')
    target_port = int(target_port)
    sock = connect_to_target(target_ip, target_port)
    while isRunning:
        command = input(f"{target_ip} >>> ")
        output = execute_command(sock, command)
        if output:
            print(output)
            continue 
        print("Something went wrong !") 


if __name__ == '__main__':
    # Authentication
    isAuthenticated = authenticate()
    if not isAuthenticated:

        sys.stdout.flush()
        exit(-1)

    # Starts terminal
    main()
