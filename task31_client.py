import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = b'test message'
addr = ('127.0.0.1', 65432)

clientSocket.sendto(data, addr)
try:
    data, addr = clientSocket.recvfrom(1024)
    print(f'Received {data}')
except socket.timeout:
    print('Connection timed out')