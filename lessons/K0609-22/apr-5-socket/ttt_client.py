import tkinter as tk
import ttkbootstrap as ttk
import socket
from time import sleep
import ttt_client_thread

mark = None

root = ttk.Window(themename="darkly")


port_ent = ttk.Entry(textvariable=tk.StringVar(value="59090"))
port_ent.grid(column=0, row=0, columnspan=2)

connect_btn = ttk.Button(text="Connect", command=lambda: connect(port_ent.get()))
connect_btn.grid(column=2, row=0)

status_var = tk.StringVar(value="Not connected")

status_lbl = ttk.Label(textvariable=status_var)
status_lbl.grid(column=0, row=1, columnspan=3)

board = []
for i in range(9):
    board.append(ttk.Button(command=lambda i=i: send(f"MESSAGE {i}")))
    board[i].grid(row=2 + i // 3, column=i % 3, sticky="wens")





root.protocol("WM_DELETE_WINDOW", ttt_client_thread.on_closing)
root.mainloop()
