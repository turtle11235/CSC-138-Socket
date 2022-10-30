#import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
serverSocket.bind(("127.0.0.1", 6789))
serverSocket.listen()

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        response = f"HTTP/1.1 200 OK\r\n\r\n{outputdata}"
        connectionSocket.send(response.encode('utf-8'))
        connectionSocket.close()

    except IOError:
        #Send response message for file not found
        connectionSocket.send(b"HTTP/1.1 404 NOT FOUND\r\n")

        #Close client socket
        connectionSocket.close()
        print("failed")