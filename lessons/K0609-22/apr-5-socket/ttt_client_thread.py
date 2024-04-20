import threading
import socket
from .ttt_client import root

sock = None


def connect(port):
    global sock, mark

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("localhost", int(port)))

        msg = receive()
        mark = msg[8]
        status_var.set(msg.split("MESSAGE")[0].strip())
        sleep(1)
        if mark == "X":
            msg = receive()
            status_var.set(msg.split("MESSAGE")[0].strip())

    except Exception as e:
        status_lbl["text"] = f"Failed: {e}"


def send(message: str):
    print(f"Sending: {message}")
    sock.send(message.encode())


def receive():
    print("Start receiving...")
    message: str = ""
    while True:
        msg = sock.recv(8)
        print(b"    " + msg)
        message += msg.decode()
        if len(msg) < 8:
            break

    message = message.strip()
    print(f"Finished receiving. Got {message}")
    return message


def client():
    pass


def on_closing():
    if sock:
        sock.close()
    root.destroy()
