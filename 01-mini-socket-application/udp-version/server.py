from socket import *

server_port = 3000

# set up UDP socket and bind process to port 3000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))
print('The server is ready to receive')

while True:
    message, client_address = server_socket.recvfrom(2048)
    modified_message = message.decode().upper()
    print('Transformed a message: ', modified_message)
    server_socket.sendto(modified_message.encode(), client_address)
