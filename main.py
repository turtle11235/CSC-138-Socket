#import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
serverSocket.bind(("127.0.0.1", 8080))
serverSocket.listen()

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = bytearray(f.read(), 'utf-8')
        # print(outputdata)

        #Send one HTTP header line into socket
        connectionSocket.send(b"HTTP/1.1 200 OK\r\n")
        #Fill in start
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            print("sending message")
            print(type(outputdata[i]))
            connectionSocket.send(outputdata[i])
            connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send(b"HTTP/1.1 404 NOT FOUND\r\n")
        
        #Close client socket
        connectionSocket.close()
        print("failed")