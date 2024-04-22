import threading
import socket
import time

COMMAND = None
TIMEOUT = 1


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
    BUF_SIZE = 10
    print("Start receiving...")
    message: str = ""
    time_start = time.time()
    while time.time() < time_start + TIMEOUT:
        msg = sock.recv(BUF_SIZE)
        while msg:
            print((b"\t" + msg).decode())
            message += msg.decode()
            if len(msg) < BUF_SIZE:
                break
            msg = sock.recv(BUF_SIZE)
        else:
            continue
        break
    else:
        print("Timed out")
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
        time_start = time.time()
        while time.time() < time_start + TIMEOUT:
            time.sleep(0.1)
            if COMMAND:
                send(sock, COMMAND)
                COMMAND = None
                break

        


def client_start(port, root):
    cl = threading.Thread(target=client_loop, args=(port, root), daemon=True)
    cl.start()
