class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.fave_song = []
        self.tab = []

    def add_song(self, song):
        self.fave_song.append(song)

    def cheer_loudly(self, room):
        for choon in room.songs:
            if self.fave_song[0] == choon:
                return "CHOOOON!"