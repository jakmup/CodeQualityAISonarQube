from music_service import User, UserMusicService

class UserMusicService:
    def __init__(self, user):
        self.user = user
        self._playback_state = None
    
    @property
    def playback_state(self):
        if self._playback_state is None:
            self._playback_state = self.user.get_playback_state()
        return self._playback_state
    
    def test_start_playback(self, song_id):
        if self.playback_state is None:
            raise ValueError("Playback state is not set")
        
        # Get the song object
        song = User.get_song_by_id(song_id)
        
        # Start the song playback
        self.user.play_song(song)
        
        # Update the playback state
        self._playback_state = song.get_playback_state()
    
    def test_pause_playback(self):
        if self.playback_state is None:
            raise ValueError("Playback state is not set")
        
        # Get the song object
        song = User.get_song_by_id(self.playback_state.song_id)
        
        # Pause the song playback
        self.user.pause_song(song)
        
        # Update the playback state
        self._playback_state = song.get_playback_state()
    
    def test_stop_playback(self):
        if self.playback_state is None:
            raise ValueError("Playback state is not set")
        
        # Get the song object
        song = User.get_song_by_id(self.playback_state.song_id)
        
        # Stop the song playback
        self.user.stop_song(song)
        
        # Update the playback state
        self._playback_state = song.get_playback_state()
    
    def test_get_playback_state(self):
        if self._playback_state is None:
            # Get the current song
            current_song = User.get_current_song()
            
            # Update the playback state
            self._playback_state = current_song.get_playback_state()
        
        return self._playback_state