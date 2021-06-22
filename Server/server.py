import socket
import sys

#create socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = ''
PORT = 6789

#bind socket and listen for connections
serverSocket.bind((HOST, PORT))
serverSocket.listen()

#
while True:
    print("Ready to serve...")

    connectionSocket, addr = serverSocket.accept()
    print("connected")

    #recieve request and try to send requested file, send error if file not found
    try:
        message = connectionSocket.recv(1000)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        connectionSocket.send('HTTP/1.1 200 OK\n'.encode())
        connectionSocket.send('Content-Type: text/html\n\n'.encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

    except IOError:
        connectionSocket.send('HTTP/1.1 404 Not Found\n'.encode())
        connectionSocket.send('Content-Type: text/html\n\n'.encode())
    
    #Close client socket
    connectionSocket.close()

    #Close server socket and exit
    serverSocket.close()
    sys.exit()
