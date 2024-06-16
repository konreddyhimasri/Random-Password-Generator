import tkinter as tk
from tkinter import messagebox, StringVar
import random
import pyperclip

def generate_password():
    length = length_var.get()
    char_type = char_type_var.get()
    exclude_chars = exclude_var.get()

    if not length.isdigit() or int(length) <= 0:
        messagebox.showerror("Invalid Input", "Please enter a valid positive integer for password length.")
        return
    
    length = int(length)

    if char_type == "Alphanumeric":
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    elif char_type == "Alphabetic":
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    elif char_type == "Numeric":
        characters = "0123456789"
    elif char_type == "Custom":
        characters ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+{}|:>?<,./;][=-~`"

    if not characters:
        messagebox.showerror("Invalid Selection", "No characters available to generate password. Please adjust your settings.")
        return

    password = "".join(random.choice(characters) for _ in range(length))
    password_var.set(password)
    
def copy_to_clipboard():
    password = password_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
        
root = tk.Tk()
root.title("Password Generator")
root.geometry("600x500")
root.configure(bg="#8a2be2")
title_label = tk.Label(root, text="Password Generator", font=("Lucida", 24, "bold"), bg="#8a2be2", fg="white")
title_label.pack(pady=20)
tk.Label(root, text="Password Length:", font=("Lucida", 14), bg="#8a2be2", fg="white").pack(anchor="w", padx=20, pady=5)
length_var = StringVar(value="12")
length_entry = tk.Entry(root, textvariable=length_var, font=("Lucida", 14))
length_entry.pack(anchor="w", padx=20, pady=5)
char_type_var = StringVar(value="Alphanumeric")# Character type dropdown
char_type_label = tk.Label(root, text="Character Type:", font=("Lucida", 14), bg="#8a2be2", fg="white")
char_type_label.pack(anchor="w", padx=20, pady=5)
char_type_options = ["Alphanumeric", "Alphabetic", "Numeric", "Custom"]
char_type_dropdown = tk.OptionMenu(root, char_type_var, *char_type_options)
char_type_dropdown.config(font=("Lucida", 12), bg="#8a2be2", fg="white", highlightbackground="#8a2be2")
char_type_dropdown.pack(anchor="w", padx=20, pady=5)
tk.Label(root, text="Exclude Characters:", font=("Lucida", 14), bg="#8a2be2", fg="white").pack(anchor="w", padx=20, pady=5)
exclude_var = StringVar(value="")
exclude_entry = tk.Entry(root, textvariable=exclude_var, font=("Lucida", 14))
exclude_entry.pack(anchor="w", padx=20, pady=5)
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#9932cc", fg="white", font=("Lucida", 14, "bold"))
generate_button.pack(pady=20)
password_var = StringVar(value="")# Generated password display
password_entry = tk.Entry(root, textvariable=password_var, font=("Lucida", 18), state="readonly", width=50)
password_entry.pack(padx=20, pady=5)
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#9932cc", fg="white", font=("Lucida", 14, "bold"))
copy_button.pack(pady=10)
root.mainloop()
