import http.client

icon = """
█▀█ █▀█ ▀▀▀█ 
░▄▀ ░▄▀ ░░█░ 
█▄▄ █▄▄ ░▐▌░
"""

def loading_bar():
    for i in range(26):
        print("[" + "#"*(i*4), "-"*(100 - i*4) +"]" ,end="\r")
    print('\n')

conn = http.client.HTTPSConnection('www.python.org', port=80, timeout=10, source_address=('127.0.0.1', 8888))
result = conn.connect()
print(result)


