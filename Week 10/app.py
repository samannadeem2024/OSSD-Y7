import tkinter as tk
from tkinter import messagebox

# login reading from file
def read_file():
    try:
        with open("users.txt", "r") as file:
            users = {}
            for line in file:
                username, password = line.strip().split(",")
                users[username] = password
            return users
    except FileNotFoundError:
        return {}

def write_file(username, password):
    with open("users.txt", "a") as file:
        file.write(username + "," + password + "\n")

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showwarning("Error", "Please fill all fields!")
        return

    users = read_file()

    if username in users and users[username] == password:
        messagebox.showinfo("Success", f"Welcome back, {username}!")
    else:
        messagebox.showerror("Error", "Invalid username or password!")

def signup():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showwarning("Error", "Please fill all fields!")
        return

    users = read_file()

    if username in users:
        messagebox.showerror("Error", "Username already exists!")
        return

    write_file(username, password)
    messagebox.showinfo("Success", "Account created successfully!")

def main():
    global username_entry, password_entry

    # Labels and Inputs
    tk.Label(root, text="Username").pack(pady=5)
    username_entry = tk.Entry(root, width=30)
    username_entry.pack(pady=5)

    tk.Label(root, text="Password").pack(pady=5)
    password_entry = tk.Entry(root, width=30, show="*")
    password_entry.pack(pady=5)

    # Buttons
    tk.Button(root, text="Login", width=15, command=login).pack(pady=10)
    tk.Button(root, text="Sign Up", width=15, command=signup).pack(pady=5)

# Main Window
root = tk.Tk()
root.title("Login System")
root.geometry("300x250")

main()
root.mainloop()