import pwinput
import sys

from Encrypt import encrypt

encrypted_admin_password = encrypt('hello')
encrypted_admin_username = encrypt('no227')


def authenticate() -> bool:
    for attempts in range(3):
        sys.stdout.write('Enter username : ')
        sys.stdout.flush()
        for line in sys.stdin:
            username = line
            break

        username = username.split('\n')[0]

        password = pwinput.pwinput(prompt='Enter password : ')

        if encrypt(username) == encrypted_admin_username and encrypt(password) == encrypted_admin_password:
            return True
    return False


def main():
    with open('bin_addr.txt', 'w') as bin_addr:
        all_commands = bin_addr.readlines()

    command_dir = {}
    for command in all_commands:
        command_dir[command.split(':')[0]] = command.split(':')[1]

    is_active = True
    while is_active:
        sys.stdout.write(command_dir)
        sys.stdout.flush()
        is_active = False


if __name__ == '__main__':
    authenticate()
    main()
