import rsa 
import socket_packets
import socket  


def send_packet(packet: bytes, receiver_socket: socket.socket) -> None:
    receiver_socket.send(packet)


def receive_requests(port: int) -> socket.socket:
    receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    receiver.bind(socket.gethostname(), port)
    receiver.listen()
    return receiver


def request_parser(receiver: socket.socket):
    bot_socket, bot_addr = receiver.accept()
    request = receiver.recv(1024)
    request = request.decode('utf-8')
    parsed_request = request.split('/')
    level, subject_id = int(parsed_request[0]), int(parsed_request[1])

