import threading
import socket
import time

COMMAND = None

def new_command(x):
    global COMMAND

    COMMAND = x


def connect(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("localhost", int(port)))
        return sock
        # msg = receive()
        # mark = msg[8]
        # status_var.set(msg.split("MESSAGE")[0].strip())
        # sleep(1)
        # if mark == "X":
        #     msg = receive()
        #     status_var.set(msg.split("MESSAGE")[0].strip())

    except Exception as e:
        print(f"Failed: {e}")


def send(sock: socket, message: str):
    print(f"Sending: {message}")
    sock.send(message.encode())
    # sock.


def receive(sock):
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


def client_loop(port, root):
    global COMMAND

    upd_status = lambda t: root.children["status"].config(text = t)
    mark = None
    opponents_mark = None

    sock = connect(port)
    if not sock:
        print("Connection error. Stopping thread.")
        upd_status("Connection error. Stopping thread.")
        return
    print("Connection established")
    upd_status("Connection established")

    root.children["!button"]["state"] = "disabled"

    while True:
        message = receive(sock)

        upd_status(message)

        if message.startswith("WELCOME"):
            mark = message[8]
            opponents_mark = "O" if mark == "X" else "X"
        elif message.startswith("OPPONENT_MOVED"):
            x = int(message[15])
            root.children[f"!button{x+2}"].config(text = opponents_mark)
        elif message.startswith("VICTORY") \
             or message.startswith("DEFEAT") \
             or message.startswith("TIE") \
             or message.startswith("OTHER_PLAYER_LEFT"):
            break
        
        # -------------------
        
        while not COMMAND:
            time.sleep(0.1)
        else:
            send(sock, COMMAND)
            COMMAND = None

        


def client_start(port, root):
    cl = threading.Thread(target=client_loop, args=(port, root), daemon=True)
    cl.start()


def on_closing():
    if sock:
        sock.close()
    root.destroy()
