from socket import *

server_name = '127.0.0.1'
server_port = 12001

client_socket = socket(AF_INET, SOCK_STREAM) # SOCK_STREAM means we're gonna use TCP
client_socket.connect((server_name, server_port))

message = input('Input lowercase sentence: ')

client_socket.send(message.encode('utf-8'))

modified_message = client_socket.recv(1024).decode('utf-8')

print("From Server: " + modified_message)

client_socket.close()