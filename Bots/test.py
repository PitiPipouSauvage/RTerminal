icon = """\
█▀█ █▀█ ▀▀▀█ 
░▄▀ ░▄▀ ░░█░ 
█▄▄ █▄▄ ░▐▌░
"""

def loading_bar():
    for i in range(26):
        print("[" + "#"*(i*4), "-"*(100 - i*4) +"]" ,end="\r")
    print('\n')


with open("new_file.txt", 'w') as f:
    f.write(icon)
