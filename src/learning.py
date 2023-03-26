import tkinter as tk

window = tk.Tk()
# greeting = tk.Label(text="Hello, Tkinter", width=50, height=20)
# bt = tk.Button(text='Click Me!', width=10, height=5)
# py = tk.Label(text='La gata!!!!',
#     foreground='red',
#     background='green')
# entry = tk.Entry(fg="yellow", bg="blue", width=50)

# frame_a = tk.Frame()
# frame_b = tk.Frame()

# label_a = tk.Label(master=frame_a, text='I\'m frame a')
# label_a.pack()
# label_b = tk.Label(master=frame_b, text='I\'m frame b')
# label_b.pack()


# border_effects = {
#     "flat": tk.FLAT,
#     "sunken": tk.SUNKEN,
#     "raised": tk.RAISED,
#     "groove": tk.GROOVE,
#     "ridge": tk.RIDGE,
# }

# for relief_name, relief in border_effects.items():
#     frame = tk.Frame(master=window, relief=relief, borderwidth=5)
#     frame.pack(side=tk.LEFT)
#     label = tk.Label(master=frame, text=relief_name)
#     label.pack()

# frame = tk.Frame(master=window, borderwidth=5)
# frame.pack(side=tk.LEFT)
# lbl = tk.Label(text="what's your name", width=40, background='white',fg='black')
# lbl.pack(side=tk.LEFT)

# frame = tk.Frame(master=window, width=150, height=150)
# frame.pack()

# label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
# label1.place(x=0, y=0)

# label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
# label2.place(x=100, y=100)

# for i in range(3):
#     window.columnconfigure(i, weight=1, minsize=75)
#     window.rowconfigure(i, weight=1, minsize=50)
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j, padx=5, pady=5)
#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack(padx=5, pady=5)

# window.rowconfigure(0, minsize=50)
# window.columnconfigure([0, 1, 2, 3], minsize=50)

# label1 = tk.Label(text="1", bg="black", fg="white")
# label2 = tk.Label(text="2", bg="black", fg="white")
# label3 = tk.Label(text="3", bg="black", fg="white")
# label4 = tk.Label(text="4", bg="black", fg="white")

# label1.grid(row=0, column=0)
# label2.grid(row=0, column=1, sticky="ew")
# label3.grid(row=0, column=2, sticky="ns")
# label4.grid(row=0, column=3, sticky="nsew")


label2 = tk.Label(text="Hello, Tkinter", width=10, height=5, bg="blue")
label = tk.Label(text="Hello, Tkinter", width=50, height=20, bg='green')
label.pack(label2.pack())

window.mainloop()