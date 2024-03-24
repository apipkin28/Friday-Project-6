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