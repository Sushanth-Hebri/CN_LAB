import socket
import os

# Server configuration
HOST = '127.0.0.1'
PORT = 12345
BUFFER_SIZE = 1024
FILE_DIRECTORY = 'server_files'

def send_file_contents(filename, client_address):
    try:
        with open(os.path.join(FILE_DIRECTORY, filename), 'rb') as file:
            data = file.read(BUFFER_SIZE)
            while data:
                server_socket.sendto(data, client_address)
                data = file.read(BUFFER_SIZE)
    except FileNotFoundError:
        error_message = "File not found"
        server_socket.sendto(error_message.encode(), client_address)

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print("Server is listening on {}:{}".format(HOST, PORT))

while True:
    data, client_address = server_socket.recvfrom(BUFFER_SIZE)
    filename = data.decode()
    
    print("Client at {} requested file: {}".format(client_address, filename))
    
    send_file_contents(filename, client_address)

server_socket.close()
