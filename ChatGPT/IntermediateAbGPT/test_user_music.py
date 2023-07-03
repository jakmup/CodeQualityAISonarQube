class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserManagement:
    def __init__(self):
        self.users = []

    def add_user(self, name, email):
        user = User(name, email)
        self.users.append(user)
        print(f"User {name} added successfully!")

    def remove_user(self, email):
        for user in self.users:
            if user.email == email:
                self.users.remove(user)
                print(f"User {user.name} removed successfully!")
                return
        print("User not found!")

    def get_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None

class MusicPlayer:
    def __init__(self):
        self.playlist = []

    def add_song(self, song):
        self.playlist.append(song)
        print(f"Song {song} added to the playlist!")

    def remove_song(self, song):
        if song in self.playlist:
            self.playlist.remove(song)
            print(f"Song {song} removed from the playlist!")
        else:
            print("Song not found in the playlist!")

    def play(self):
        if self.playlist:
            print("Playing music...")
            for song in self.playlist:
                print(f"Now playing: {song}")
        else:
            print("Playlist is empty!")

class UserMusicService:
    def __init__(self):
        self.user_management = UserManagement()
        self.music_player = MusicPlayer()

    def add_user(self, name, email):
        self.user_management.add_user(name, email)

    def remove_user(self, email):
        self.user_management.remove_user(email)

    def get_user_by_email(self, email):
        return self.user_management.get_user_by_email(email)

    def add_song(self, song):
        self.music_player.add_song(song)

    def remove_song(self, song):
        self.music_player.remove_song(song)

    def play(self):
        self.music_player.play()

# Create an instance of UserMusicService
user_music_service = UserMusicService()

# Add a user
user_music_service.add_user("John", "john@example.com")

# Add a song
user_music_service.add_song("Song 1")

# Play music
user_music_service.play()

# Remove a user
user_music_service.remove_user("john@example.com")
