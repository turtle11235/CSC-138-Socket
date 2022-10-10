from socket import *

server_port = 12001
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))

print("The server is ready to receive")

while True:
    message, client_address = server_socket.recvfrom(2048)
    modified_message = message.upper()
    server_socket.sendto(modified_message, client_address)
