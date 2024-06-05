from socket import *
import sys
import threading

# Function to handle client requests in separate threads
def handle_client(connectionSocket, addr):
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        print(filename)
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
        # Send HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        # Send the content of the requested file to the client
        connectionSocket.send(outputdata.encode())

        connectionSocket.close()
    except IOError or FileNotFoundError:
        # Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.close()

# Main function to listen for incoming connections
def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverPort = 5500
    serverSocket.bind(('localhost', serverPort))
    serverSocket.listen(1)
    print('The server is ready to receive')

    while True:
        # Establish the connection
        connectionSocket, addr = serverSocket.accept()
        print('Connection received from:', addr,'\n')

        # Create a new thread for each client connection
        client_thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
        client_thread.start()
        print(f'[ACTIVE CONNECTION] {threading.active_count()-1}')

    serverSocket.close()
    sys.exit()

if __name__ == "__main__":
    main()