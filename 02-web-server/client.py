from socket import *
import sys

hostname = sys.argv[1]
port = int(sys.argv[2])

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((hostname, port))

client_socket.send(f'GET {sys.argv[3]} HTTP/1.1\r\n'.encode())
client_socket.send(f'Host: {hostname}\r\n\r\n'.encode())
response = client_socket.recv(1024).decode()
print(response)

client_socket.close()
