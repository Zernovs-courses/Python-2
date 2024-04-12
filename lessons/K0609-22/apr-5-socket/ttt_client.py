import tkinter as tk
import ttkbootstrap as ttk
import socket
from time import sleep

sock = None
mark = None


def connect(port):
    global sock, mark

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("localhost", int(port)))

        msg = receive()
        mark = msg[8]
        status_lbl["text"] = msg.split("MESSAGE")[0].strip()

        if mark == 'X':
            msg = receive()
            status_lbl["text"] = msg.split("MESSAGE")[0].strip()

    except Exception as e:
        status_lbl["text"] = f"Failed: {e}"


def send(message: str):
    print(f"Sending: {message}")
    sock.send(message.encode())


def receive():
    print('Start receiving...')
    message: str = ""
    while True:
        msg = sock.recv(8)
        print(b"    " + msg)
        message += msg.decode()
        if len(msg) < 8:
            break
    
    message = message.strip()
    print(f'Finished receiving. Got {message}')
    return message


root = ttk.Window(themename="darkly")


port_ent = ttk.Entry(textvariable=tk.StringVar(value="59090"))
port_ent.grid(column=0, row=0, columnspan=2)

connect_btn = ttk.Button(text="Connect", command=lambda: connect(port_ent.get()))
connect_btn.grid(column=2, row=0)

status_lbl = ttk.Label(text="Not connected")
status_lbl.grid(column=0, row=1, columnspan=3)

board = []
for i in range(9):
    board.append(ttk.Button(command=lambda i=i: send(f"MESSAGE {i}")))
    board[i].grid(row=2 + i // 3, column=i % 3, sticky="wens")


def on_closing():
    if sock:
        sock.close()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
