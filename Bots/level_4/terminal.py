import pwinput
import os
import socket
import subprocess
import sys
import threading 

from Encrypt import encrypt

encrypted_admin_password = encrypt('hello')
encrypted_admin_username = encrypt('no227')


def authenticate():
    sys.stdout.write('Enter username : ')
    for line in sys.stdin:
        username = line
        break

    password = pwinput.pwinput(prompt='Enter password : ')
    print(password)


def main():
    with open('./bin_addr.txt', 'w') as bin_addr:
        all_commands = bin_addr.readlines()

    command_dir = {}
    for command in all_commands:
        command_dir[command.split(':')[0]] = command.split(':')[1]

    is_active = True
    while is_active:
        sys.stdout.write('') 


if __name__ == '__main__':
    authenticate()
    os.system('pause')
