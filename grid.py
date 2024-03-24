import tkinter as tk

# main window
root = tk.Tk()
root.title("Sign-Up Page")

def signup():
    name = nameEntry.get()
    email = emailEntry.get()
    password = passwordEntry.get()

# retrieved values
    print("Name:", name)
    print("Email:", email)
    print("Password:", password)