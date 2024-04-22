import threading
import socket


ROOT = None
CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
MARK = None
OPPONENT_MARK = None
upd_status = lambda t: ROOT.children["status"].config(text = t)
LAST_CELL = None

def connect(port):
    try:
        CLIENT.connect(("localhost", int(port)))
    except Exception as e:
        print(f"Failed: {e}")


def send_command(command):
    global LAST_CELL

    LAST_CELL = int(command[5:])
    print(command)


    sending_thread = threading.Thread(target = send, args = (command,))
    sending_thread.start()


def send(*args):
    message = "".join(args)
    print(f"Sending: {message}")
    while True:
        try:
            CLIENT.send(message.encode())
            break
        except:
            pass

def process_message(message):
    global MARK, OPPONENT_MARK

    print(message)
    if message.startswith("WELCOME"):
        MARK = message[8]
        OPPONENT_MARK = "O" if MARK == "X" else "X"
    elif message.startswith("OPPONENT_MOVED"):
        x = int(message[15])
        ROOT.children[f"!button{x+2}"].config(text = OPPONENT_MARK)
    elif message.startswith("VICTORY") \
            or message.startswith("DEFEAT") \
            or message.startswith("TIE") \
            or message.startswith("OTHER_PLAYER_LEFT"):
        pass
    elif message.startswith("VALID MOVE"):
        ROOT.children[f"!button{LAST_CELL+2}"].config(text = MARK)

    upd_status(message)

def receive():
    print("Start receiving...")
    while True:
        message = CLIENT.recv(1024).decode().strip()
        if message:
            process_message(message)


def client_start(port, root):
    global ROOT

    ROOT = root
    
    CLIENT.connect(("localhost", int(ROOT.children["!entry"].get())))
    if not CLIENT:
        upd_status("Connection error. Stopping")
        return
    upd_status("Connection established")

    receiving_thread = threading.Thread(target = receive, daemon = True)
    receiving_thread.start()
