import sys
import socket

if len(sys.argv) != 2:
    print('Pass server IP as argument')
else:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((sys.argv[1], 59898))
        print('Ctrl+C or Ctrl+D to exit')
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            sock.sendall(line.encode())
            while True:
                data = sock.recv(128)
                print(data.decode(), end='')
                if len(data) < 128:
                    break