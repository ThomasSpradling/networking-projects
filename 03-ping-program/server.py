import random
from socket import *

server_port = 3000

# create UDP socket
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))
print('The server is ready to receive')

while True:
    message, client_address = server_socket.recvfrom(2048)
    modified_message = message.decode().upper()

    # 30% of the time, simulate a packet loss
    if random.randint(0, 10) <= 3:
        continue
    server_socket.sendto(modified_message.encode(), client_address)
