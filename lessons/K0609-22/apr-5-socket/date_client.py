import sys
import socket


if len(sys.argv) != 3:
    print('Pass the server IP')
else:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((sys.argv[1], int(sys.argv[2])))
        print(sock.recv(1024))