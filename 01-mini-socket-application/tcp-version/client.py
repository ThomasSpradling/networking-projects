from socket import *

hostname = 'localhost'
port = 3000

# set up TCP socket and handshake (connect)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((hostname, port))

# grab user input and send to server
message = input('Input lowercase sentence: ')
client_socket.send(message.encode())

modified_message = client_socket.recv(1024)
print(modified_message.decode())
client_socket.close()
