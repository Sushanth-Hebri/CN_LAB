import socket
import os

# Server configuration
server_host = '127.0.0.1'
server_port = 12345
buffer_size = 1024

# Function to handle client requests
def handle_client(client_socket):
    # Receive the requested file name from the client
    file_name = client_socket.recv(buffer_size).decode()
    
    # Check if the file exists
    if os.path.isfile(file_name):
        # If the file exists, send its contents back to the client
        with open(file_name, 'rb') as file:
            data = file.read(buffer_size)
            while data:
                client_socket.send(data)
                data = file.read(buffer_size)
    else:
        # If the file does not exist, send an error message
        client_socket.send(b'File not found')
    
    client_socket.close()

# Main server loop
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_host, server_port))
    server.listen(5)
    print(f"Server listening on {server_host}:{server_port}")

    while True:
        client_socket, client_addr = server.accept()
        print(f"Accepted connection from {client_addr[0]}:{client_addr[1]}")
        handle_client(client_socket)

if __name__ == "__main__":
    main()
