import tkinter as tk

# User data storage
users = []

# User authentication code
def login():
    username = username_entry.get()
    password = password_entry.get()

    for user in users:
        if user.username == username and user.password == password:
            result_label.config(text="Login successful")
            return

    result_label.config(text="Invalid credentials")

# User profile management code
def update_profile(username, profile_data):
    for user in users:
        if user.username == username:
            user.profile_data = profile_data

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

update_profile_button = tk.Button(window, text="Update Profile", command=lambda: update_profile(username_entry.get(), profile_entry.get()))
update_profile_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Start the main event loop
window.mainloop()