#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("500x200")

# create empty frame
frame_login = tk.Frame(root)
frame_auth = tk.Frame(root)
frame_auth.grid(column=0, row=0, stick="news")


#(new window for components in toot)
frame_login.grid()


def login():
    frame_auth.tkraise()

#Widgets for frame login
lbl_username = tk.Label(frame_login, text="Username", fg="red", font="Helvetica 20")
lbl_username.pack(padx=35)

#Text box for username
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

#Widgeets frane log
lbl_password = tk.Label(frame_login, text="Password", fg="blue", font="Helvetica 20")
lbl_password.pack(padx=185)

#Text box for password
ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack(pady=5)


button_login = tk.Button(frame_login, text="login", command=login)
button_login.pack(pady=5)

lbl_authorized = tk.Label(frame_login, text="Authorization Screen", fg="blue", font="Helvetica 20")
lbl_authorized.pack(padx=185)


frame_login.tkraise()
root.mainloop()