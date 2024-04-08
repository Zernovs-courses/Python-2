import sys
import socket

if len(sys.argv) != 2:
    print('Pass server IP as argument')
else:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((sys.argv[1], 59090))
        print(sock.recv(1024).decode())