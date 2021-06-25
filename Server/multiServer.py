import socket
import threading

# This is a multithreaded server that will accept incoming request, start a new thread and then
# serve that request through a new port

HOSTNAME = ''
PORT = 6789

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOSTNAME, PORT))

#function to call for new connection thread
def clientHandler(connectionSocket, addr):
    try:
        print(f"Connected Device: {addr[0]}\nOn Port: {addr[1]}")
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

    connectionSocket.close()
    

#Launch server and set socket to listen. Will start a new thread for each incoming connection
server_socket.listen()
print("Ready to serve...")
while True:
    connectionSocket, addr = server_socket.accept()
    newThread = threading.Thread(target= clientHandler, args = (connectionSocket, addr))
    newThread.start()



