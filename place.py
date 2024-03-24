import tkinter as tk

# main window
root = tk.Tk()
root.title("Log-in Page")

def login():
    username = usernameEntry.get()
    password = passwordEntry.get()
    # retrieve values
    print("Username:", username)
    print("Password:", password)

# label and entry widgets
usernameLabel = tk.Label(root, text="Username:")
usernameLabel.place(x=50, y=50)

usernameEntry = tk.Entry(root)
usernameEntry.place(x=150, y=50)

passwordLabel = tk.Label(root, text="Password:")
passwordLabel.place(x=50, y=80)

passwordEntry = tk.Entry(root, show="*")
passwordEntry.place(x=150, y=80)