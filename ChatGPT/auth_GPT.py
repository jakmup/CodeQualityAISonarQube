# auth.py module

# User data storage
users = []

# User class representing a user object
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def authenticate(username, password):
    for user in users:
        if user.username == username and user.password == password:
            return True
    return False

def register_user(username, password):
    for user in users:
        if user.username == username:
            return False

    new_user = User(username, password)
    users.append(new_user)
    return True
