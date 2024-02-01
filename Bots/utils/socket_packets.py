from cryptography.fernet import Fernet
from random import randint

levels = [i for i in range(5)]

subjects = [
    "command",
    "roles",
    "procedures"
]


def generate_random_string(length=40) -> str:
    """This function is used to generate a new key for the fernet to encrypt the body of the message"""
    characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-&`'
    characters_length = len(characters)
    random_string = ''
    for i in range(length):
        random_string += characters[randint(0, characters_length - 1)]
    return random_string


def generate_id(used_ids, length=10) -> int:
    """This function is used to generate a message id"""
    id = used_ids[-1] + 1
    number_length = len(str(id))
    while number_length > 10:
        number_length -= 10

    id = f"{'0' * 10 - number_length}{str(id)}"
    used_ids.append(int(id))
    return int(id) 


def generate_header(level: int, subject_id: int) -> tuple:
    """This function generates a header exclusivly in numbers"""
    new_key = generate_random_string()
    header = f"{str(level)}/{str(subject_id)}/{new_key}"
    fernet = Fernet(b'cw_0x689RpI-jtRR7oE8h_eQsKImvJapLeSbXpwF4e4=')
    encrypted_header = fernet.encrypt(header.encode('utf-8'))
    return encrypted_header, new_key


def generate_package(header: bytes, message: str, message_key: bytes) -> bytes:
    """This function generates the full package ready to be sent"""
    message_fernet = Fernet(message_key)
    encrypted_body = message_fernet.encrypt(message.encode('utf-8'))
    encrypted_message = f'{header}/{encrypted_body}'
    return encrypted_message
