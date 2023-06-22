import tkinter as tk
from auth_GPT import authenticate, register_user
from user_profile_GPT import UserProfile

def login():
    username = username_entry.get()
    password = password_entry.get()

    if authenticate(username, password):
        result_label.config(text="Login successful")
    else:
        result_label.config(text="Invalid credentials")

def register():
    username = username_entry.get()
    password = password_entry.get()

    if register_user(username, password):
        result_label.config(text="Registration successful")
    else:
        result_label.config(text="Username already exists. Please choose a different username.")

# Create the main window
window = tk.Tk()
window.title("User Management")

# Create and position UI elements
login_label = tk.Label(window, text="Username:")
login_label.pack()

username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Password:")
password_label.pack()

password_entry = tk.Entry(window, show="*")
password_entry.pack()

login_button = tk.Button(window, text="Login", command=login)
login_button.pack()

register_button = tk.Button(window, text="Register", command=register)
register_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Start the main event loop
window.mainloop()
