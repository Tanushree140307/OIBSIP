import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    chars = ""

    if var_letters.get():
        chars += string.ascii_letters
    if var_numbers.get():
        chars += string.digits
    if var_symbols.get():
        chars += string.punctuation

    if not chars:
        result_label.config(text="Select at least one option!")
        return

    password = "".join(random.choice(chars) for _ in range(length))
    result_label.config(text=password)

# Window
root = tk.Tk()
root.title("Password Generator")

# Center + Square
window_width = 400
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# UI Elements
tk.Label(root, text="Password Length").pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack()

var_letters = tk.BooleanVar()
var_numbers = tk.BooleanVar()
var_symbols = tk.BooleanVar()

tk.Checkbutton(root, text="Letters", variable=var_letters).pack()
tk.Checkbutton(root, text="Numbers", variable=var_numbers).pack()
tk.Checkbutton(root, text="Symbols", variable=var_symbols).pack()

tk.Button(root, text="Generate", command=generate_password).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()