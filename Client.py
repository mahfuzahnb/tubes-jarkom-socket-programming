import socket
import sys

def http_client(server_host, server_port, requested_file):
    # Membuat socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Terhubung ke server
    client_socket.connect((server_host, server_port))

    # Membuat permintaan HTTP GET
    input()
    request = f"GET {requested_file} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
    client_socket.sendall(request.encode())

    # Menerima respons dari server
    response = b''
    while True:
        part = client_socket.recv(1024)
        if not part:
            break
        response += part

    # Menampilkan respons
    print("Response:")
    print(response.decode(errors='ignore'))

    # Menutup koneksi
    client_socket.close()

if __name__ == '__main__':
    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

    http_client(server_host, server_port, filename)

