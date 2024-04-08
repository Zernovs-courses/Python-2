import tkinter as tk

import ttkbootstrap as ttk
from functools import partial


# root = tk.Tk()
root = ttk.Window(resizable=(0, 0), themename="darkly")
root.geometry("400x400")

value = tk.Variable()

op1 = None
oper = None


def calc(cmd: str):
    global op1, oper

    print(f"pressed {cmd}")
    if cmd.isdigit() or cmd == ".":
        value.set(value=value.get() + cmd)
    else:
        if op1 and oper:
            value.set(str(eval(op1 + oper + value.get())))
            op1 = None
            oper = None
        else:
            op1 = value.get()
            oper = cmd
            value.set("")


ent = ttk.Entry(textvariable=value)
ent.grid(row=0, column=0, columnspan=4)

btns = "789/456*123-0.=+"
for i in range(len(btns)):
    a = btns[i]
    btn = ttk.Button(
        text=btns[i],
        command=partial(calc, btns[i]),
        bootstyle="success" if btns[i] == "=" else ""
    ).grid(row=1 + i // 4, column=i % 4, sticky="wens")


root.mainloop()
