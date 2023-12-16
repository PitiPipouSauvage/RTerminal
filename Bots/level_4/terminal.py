import os
import pwinput
import sys

from Encrypt import encrypt


users = {
    encrypt('no227'): encrypt('hello')
}


def authenticate() -> bool:
    for attempts in range(3):
        sys.stdout.write('Enter username : ')
        sys.stdout.flush()
        for line in sys.stdin:
            username = line
            break

        username = username.split('\n')[0]

        password = pwinput.pwinput(prompt='Enter password : ')

        for user_id in range(len(list(users.keys()))):
            if list(users.keys())[user_id] == encrypt(username):
                if list(users.values())[user_id] == encrypt(password):
                    return True
            break
        sys.stdout.write(f'You have {3 - attempts} attempts remaining \n')
        sys.stdout.flush()
    return False


def main():
    with open('bin_addr.txt', 'r') as bin_addr:
        all_commands = bin_addr.readlines()

    command_dir = {}
    for command in all_commands:
        command_dir[command.split(':')[0]] = command.split(':')[1]

    is_active = True
    while is_active:
        for i in command_dir.items():
            sys.stdout.write(f'{i[0]} : {i[1]}')
            sys.stdout.flush()
        is_active = False


if __name__ == '__main__':
    # Authentication
    isAuthenticated = authenticate()
    if not isAuthenticated:
        sys.stdout.write('Either your username or password is incorrect \n')
        sys.stdout.flush()
        exit(-1)

    # Starts terminal
    main()
