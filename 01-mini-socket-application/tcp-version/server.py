from socket import *

server_port = 3000

# set up TCP socket and bind process to port 3000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))

# listen for connection requests from client
server_socket.listen(1)
print('The server is ready to receive')

while True:
    # creates new socket and establish TCP connection
    connection_socket, client_address = server_socket.accept()

    # receive and send messages
    modified_message = connection_socket.recv(1024).decode().upper()
    print('Transformed a message: ', modified_message)
    connection_socket.send(modified_message.encode())
    connection_socket.close()
