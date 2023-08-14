from socket import *
from time import time

REQUESTS_SENT = 10


def send_ping(i: int, client_socket: socket, hostname: str, port: int) -> float:
    send_time = time()
    client_socket.sendto(f'Ping {i} {send_time}'.encode(), (hostname, port))

    try:
        message, server_address = client_socket.recvfrom(2048)
        recv_time = time()

        # round trip time
        rtt = round((recv_time - send_time)*1000, 2)
        byte_count = len(message)
        print(f'{byte_count} bytes from {hostname}:{port}: udp_seq={i} time={rtt} ms')
        return rtt
    except timeout:
        print(f'Request timed out for udp_seq {i}')
        return float('inf')


hostname = 'localhost'
port = 3000
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1.0)

print(f'PING {hostname}:{port}\n\n')

# keep rolling statistics
minimum = float('inf')
maximum = 0
total = 0
survived = 0

for i in range(1, REQUESTS_SENT + 1):
    rtt = send_ping(i, client_socket, hostname, port)
    if rtt != float('inf'):
        minimum = min(minimum, rtt)
        maximum = max(maximum, rtt)
        total += rtt
        survived += 1

average = round(total / survived, 2) if survived > 0 else float('inf')
packet_loss = round((REQUESTS_SENT - survived) / REQUESTS_SENT * 100, 0)

print(f'\n\n--- {hostname} ping statistics ---')
print(f'{REQUESTS_SENT} packets transmitted, {survived} received, {packet_loss}% packet loss')
if minimum != float('inf'):
    print(f'round-trip min/avg/max = {minimum}/{average}/{maximum} ms')
