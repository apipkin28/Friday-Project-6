import tkinter as tk

# main window
root = tk.Tk()
root.title("Calculator")

def clickBtn(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(number))

def clearBtn():
    entry.delete(0, tk.END)

def equalBtn():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

entry = tk.Entry(root, width=20, state='disabled')
entry.pack(side=tk.TOP, pady=10)