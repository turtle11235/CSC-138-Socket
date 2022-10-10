from socket import *

server_name = '127.0.0.1'
server_port = 12001

client_socket = socket(AF_INET, SOCK_DGRAM) # SOCK_DGRAM means we're using UDP

message = input('Input lowercase sentence: ')

client_socket.sendto(message.encode('utf-8'), (server_name, server_port))

modified_message, server_address = client_socket.recvfrom(2048)

print(modified_message.decode())

client_socket.close()