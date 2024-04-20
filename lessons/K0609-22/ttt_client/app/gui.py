import tkinter as tk
import ttkbootstrap as ttk

from .nosock import client_start, new_command

mark = None


def build():
    root = ttk.Window(themename="darkly")

    port_ent = ttk.Entry(textvariable=tk.StringVar(value="59091"))
    port_ent.grid(column=0, row=0, columnspan=2)

    connect_btn = ttk.Button(text="Connect", command=lambda: client_start(port_ent.get(), root))
    # connect_btn = ttk.Button(text="Connect")
    connect_btn.grid(column=2, row=0)

    status_var = tk.StringVar(master=root, value="Not connected")

    # status_lbl = ttk.Label(name="status", textvariable=status_var)
    status_lbl = ttk.Label(name="status", text="Not connected")
    status_lbl.grid(column=0, row=1, columnspan=3)
    board = []
    for i in range(9):
        board.append(ttk.Button(command=lambda i=i: new_command(f"MOVE {i}")))
        # board.append(ttk.Button())
        board[i].grid(row=2 + i // 3, column=i % 3, sticky="wens")


    # root.protocol("WM_DELETE_WINDOW", ttt_client_thread.on_closing)
    print(root.children)
    return root