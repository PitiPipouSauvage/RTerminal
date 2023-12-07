import os
import socket
import subprocess
import sys
import threading 

sys.path.insert(1, '../utils/')
from Encrypt import encrypt

encrypted_admin_password = encrypt('hello')
encrypted_admin_username = encrypt('no227')

def authenticate():
    sys.stdout.write('Enter username : ')
    for line in list(sys.stdin):
        if line == '\n':
            break
        print(line)

    print('end')

def main():
    with open('./bin_addr.txt', 'w') as bin_addr:
        all_commands = bin_addr.readlines()

    command_dir = {}
    for command in all_commands:
        command_dir[command.split(':')[0]] = command.split(':')[1]

    isActive = True
    while isActive:
        sys.stdout.write('') 

if __name__ == '__main__':
    authenticate()
