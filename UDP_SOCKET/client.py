import socket

# Client configuration
HOST = '127.0.0.1'
PORT = 12345
BUFFER_SIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    filename = input("Enter the filename to request (or 'quit' to exit): ")

    if filename.lower() == 'quit':
        break

    client_socket.sendto(filename.encode(), (HOST, PORT))

    data, server_address = client_socket.recvfrom(BUFFER_SIZE)
    response = data.decode()

    if response == "File not found":
        print("File not found on the server.")
    else:
        print("Received data from the server:")
        print(response)

client_socket.close()
