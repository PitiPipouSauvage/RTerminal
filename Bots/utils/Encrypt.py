import hashlib
import argparse
import sys


def encrypt(string) -> str:
    new_string = hashlib.sha512(string.encode('utf-8'))
    new_string = new_string.hexdigest()
    return new_string


def main():
    parser = argparse.ArgumentParser(prog='encrypt.py')

    parser.add_argument('-s', '--string')
    args = parser.parse_args()

    initial_string = args[0]
    encrypted_string = encrypt(initial_string)

    sys.stdout.write(encrypted_string)

