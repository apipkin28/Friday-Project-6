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

# label and entry widgets
nameLabel = tk.Label(root, text="Name:")
nameLabel.grid(row=0, column=0, sticky="w", padx=10, pady=5)

nameEntry = tk.Entry(root)
nameEntry.grid(row=0, column=1, padx=10, pady=5)

emailLabel = tk.Label(root, text="Email:")
emailLabel.grid(row=1, column=0, sticky="w", padx=10, pady=5)

emailEntry = tk.Entry(root)
emailEntry.grid(row=1, column=1, padx=10, pady=5)

passwordLabel = tk.Label(root, text="Password:")
passwordLabel.grid(row=2, column=0, sticky="w", padx=10, pady=5)

passwordEntry = tk.Entry(root, show="*")
passwordEntry.grid(row=2, column=1, padx=10, pady=5)