import tkinter as tk

# User data storage
users = []

# User class representing a user object
class User:
    def __init__(self, username, password, profile_data):
        self.username = username
        self.password = password
        self.profile_data = profile_data

def login():
    username = username_entry.get()
    password = password_entry.get()

    for user in users:
        if user.username == username and user.password == password:
            result_label.config(text="Login successful")
            return

    result_label.config(text="Invalid credentials")

def register():
    username = username_entry.get()
    password = password_entry.get()

    for user in users:
        if user.username == username:
            result_label.config(text="Username already exists. Please choose a different username.")
            return

    new_user = User(username, password, {})
    users.append(new_user)
    result_label.config(text="Registration successful")

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