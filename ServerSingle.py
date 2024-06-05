from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket 
serverPort = 5500
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(5)
print('The server is ready to receive')

while True:
    # Establish the connection
    print("Ready to serve...")
    
    # Accept the connection
    connectionSocket, addr = serverSocket.accept()
    print(f'Connection received from: {addr}')

    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
        # Send HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        # Send content of the requested file to the client
        connectionSocket.send(outputdata.encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        
        # Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit()
