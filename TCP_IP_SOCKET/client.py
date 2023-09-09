import socket

# Client configuration
server_host = '127.0.0.1'
server_port = 12345
buffer_size = 1024

# Function to request a file from the server
def request_file(file_name):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_host, server_port))
    
    # Send the requested file name to the server
    client.send(file_name.encode())
    
    # Receive and save the file content
    with open('received_' + file_name, 'wb') as file:
        data = client.recv(buffer_size)
        while data:
            file.write(data)
            data = client.recv(buffer_size)
    
    print(f"File '{file_name}' received and saved as 'received_{file_name}'")
    client.close()

def main():
    file_name = input("Enter the file name to request from the server: ")
    request_file(file_name)

if __name__ == "__main__":
    main()
