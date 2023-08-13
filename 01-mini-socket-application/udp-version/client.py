from socket import *

hostname = 'localhost'
port = 3000

# set up UDP socket
client_socket = socket(AF_INET, SOCK_DGRAM)

# grab user input and send to server
message = input('Input lowercase sentence: ')
client_socket.sendto(message.encode(), (hostname, port))

modified_message, server_address = client_socket.recvfrom(2048)
print(modified_message.decode())
client_socket.close()
