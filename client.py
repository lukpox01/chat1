import socket

HOST = input('Server IP: ')  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(f"{input('Input: ')}".encode('utf-8'))
        data = s.recv(1024)
        print(f"Received {data!r}")