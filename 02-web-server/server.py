from socket import *
import threading
import sys


def handle_client(connection_socket: socket):
    try:
        message = connection_socket.recv(1024).decode()

        # Taking advantage of that header starts
        # with `GET <filename> HTTP/1.1`
        filename = message.split()[1]
        f = open(filename[1:])
        output_data = f.read()

        # Send HTTP response
        connection_socket.send('HTTP/1.1 200 OK\r\n'.encode())
        connection_socket.send('Content-Type: text/html\r\n\r\n'.encode())
        connection_socket.send(output_data.encode())
        connection_socket.send('\r\n'.encode())

        connection_socket.close()
    except IOError:
        # Respond with 404 Error
        connection_socket.send('HTTP/1.1 404 Not Found\r\n'.encode())
        connection_socket.close()


server_port = 3000

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(5)

while True:
    print(f'Ready to serve at port {server_port}...')
    connection_socket, client_address = server_socket.accept()

    client_thread = threading.Thread(
        target=handle_client,
        args=(connection_socket,)
    )
    client_thread.start()

server_socket.close()
sys.exit()
