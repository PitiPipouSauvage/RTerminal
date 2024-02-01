import socket
import rsa
from cryptography.fernet import Fernet

from random import randint

levels = [i for i in range(5)]

subjects = [
    "command",
    "roles",
    "procedures"
]


def generate_random_string(length=40):
    characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-&`'
    characters_length = len(characters)
    random_string = ''
    for i in range(length):
        random_string += characters[randint(0, characters_length - 1)]
    return random_string


def generate_random_number(used_ids, length=10):
    numbers = '0123456789'
    numbers_length = len(numbers)
    random_number = ''
    for i in range(length):
        random_number += numbers[randint(0, numbers_length - 1)]
    random_number = int(random_number)
    if random_number in used_ids:
        generate_random_number(used_ids, length)

    used_ids.append(random_number)
    return random_number


def generate_header(level: int, subject_id: int) -> tuple
    new_key = generate_random_string()
    header = f"{str(level)}/{str(subject_id)}/{new_key}"
    fernet = Fernet(b'cw_0x689RpI-jtRR7oE8h_eQsKImvJapLeSbXpwF4e4=')
    encrypted_header = fernet.encrypt(header.encode('utf-8'))
    return encrypted_header, new_key

def generate_message(header: bytes, message: str)

