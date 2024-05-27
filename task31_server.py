import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = '127.0.0.1'
PORT = 65432

serverSocket.bind((HOST, PORT))

while True:
    data, addr = serverSocket.recvfrom(1024)
    data = data.upper()
    serverSocket.sendto(data, addr)
    if not data:
        break

serverSocket.close()