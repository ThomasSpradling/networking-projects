from socket import *
import ssl
import base64

# globals
sender = 'example@example.com'
receiver = 'example@example.edu'
password = 'password'
mail_server = 'smtp.example.com'


def assert_response(client_socket: socket, expected_response: str):
    msg = client_socket.recv(1024).decode()
    print(msg)
    if msg[:3] != expected_response:
        print(
            f'ERROR: {expected_response} reply not received from server.')
        client_socket.close()
        exit(1)


# establish TCP connection
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((mail_server, 25))

# initial connection
assert_response(client_socket, '220')

# handshake
client_socket.send('EHLO example\r\n'.encode())
assert_response(client_socket, '250')

# Start TLS
client_socket.send('STARTTLS\r\n'.encode())
assert_response(client_socket, '220')

# Wrap the socket with SSL for encryption
client_socket = ssl.wrap_socket(client_socket)

# Re-handshake after STARTTLS
client_socket.send('EHLO example\r\n'.encode())
assert_response(client_socket, '250')

# Authenticate using your Gmail username and password
email_encoded = base64.b64encode(sender.encode()).decode()
password_encoded = base64.b64encode(password.encode()).decode()

client_socket.send('AUTH LOGIN\r\n'.encode())
assert_response(client_socket, '334')
client_socket.send((email_encoded + '\r\n').encode())
assert_response(client_socket, '334')
client_socket.send((password_encoded + '\r\n').encode())
assert_response(client_socket, '235')

# acknowledge sender
client_socket.send(f'MAIL FROM: <{sender}>\r\n'.encode())
assert_response(client_socket, '250')

# acknowledge receiver
client_socket.send(f'RCPT TO: <{receiver}>\r\n'.encode())
assert_response(client_socket, '250')

# Begin data transmission
client_socket.send('DATA\r\n'.encode())
assert_response(client_socket, '354')

# send data
while True:
    line = input()
    client_socket.send(line.encode() + '\r\n'.encode())
    if line == '.':
        break
assert_response(client_socket, '250')

# quit
client_socket.send('QUIT\r\n'.encode())
assert_response(client_socket, '221')
