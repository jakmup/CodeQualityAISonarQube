import tkinter as tk

class User:
    def __init__(self, username, password, profile_data):
        self.username = username
        self.password = password
        self.profile_data = profile_data

class UserManager:
    def __init__(self):
        self.users = []

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

    def register(self, username, password):
        new_user = User(username, password, {})
        self.users.append(new_user)
        return new_user

def create_ui():
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

    login_button = tk.Button(window, text="Login", command=lambda: login(username_entry.get(), password_entry.get()))
    login_button.pack()

    register_button = tk.Button(window, text="Register", command=lambda: register(username_entry.get(), password_entry.get()))
    register_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

    UserManager().users = []

    return window

if __name__ == "__main__":
    window = create_ui()
    window.mainloop()