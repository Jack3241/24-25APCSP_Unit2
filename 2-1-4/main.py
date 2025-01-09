#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x200")

# create empty frame
frame_login = tk.Frame(root)

#(new window for components in toot)
frame_login.grid()

#Widgets for frame login
lbl_username = tk.Label(frame_login, text="Username", fg="red", font="Helvetica 20")
lbl_username.pack(padx=35,pady=50)

#Text box for username
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)



root.mainloop()