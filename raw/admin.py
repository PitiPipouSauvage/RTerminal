import mariadb
import pwinput
import socket 
import sys
from utils.Encrypt import encrypt


def connect_to_clients_db() -> tuple:
    try:
        conn = mariadb.connect(
            user="checker",
            password="checker",
            host=sys.argv[1],
            port=sys.argv[2],
            database=clients
            )

    except:
        raise ValueError('Incorect server ip or port')

    cursor = conn.cursor()
    return cursor, conn


def check_if_client_exists(client_ip: str) -> bool:
    cursor, conn = connect_to_clients_db()
    cursor.execute('SELECT id FROM clients WHERE ip=?', (client_ip))

    if len(result) == 1:
        return True
    return False

def connect_to_admins_db(server_ip: str, server_port=3306) -> tuple:
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
    return cursor, conn


def get_user(server_ip: str, username: str, password: str, server_port=3306) -> bool:
    cursor, conn = connect_to_admins_db(server_ip, server_port)
    cursor.execute('SELECT username, password FROM admins WHERE username=? AND password=?', (username, encrypt(password)))
    result = [(username, password) for username, password in cursor]
    conn.close()
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


def connect_to_target(target_ip, target_port) -> socket.socket:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target_ip, target_port))

    return sock


def execute_command(sock: socket.socket, command: str) -> str:
    command += 'END'
    total_sent = 0
    while total_sent < len(command):
        sent = sock.send(command.encode()[total_sent:])
        if sent == 0:
            return False 
        total_sent += sent 
    
    output = b''
    while output[-3:] != b'END':
        buffer = sock.recv(2048)
        output += buffer 
    
    sock.close()
    return output  


def main() -> None:
    isRunning = True 
    target_ip, target_port = input("Enter target ip and port as such <target_ip> <target_port> : ").split(' ')
    target_port = int(target_port)
    if check_if_client_exists(target_ip):    
        while isRunning:
            sock = connect_to_target(target_ip, target_port)
            command = input(f"[{target_ip}]>>> ")
            output = execute_command(sock, command)
            if output:
                print(output)
                continue 
            print("Something went wrong !") 
        sock.close()
    else:
        exit(-1)


if __name__ == '__main__':
    # Authentication
    isAuthenticated = authenticate()
    if not isAuthenticated:

        sys.stdout.flush()
        exit(-1)

    # Starts terminal
    main()
