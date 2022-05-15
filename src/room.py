class Room:
    def __init__(self, room_name, capacity, entry_fee):
        self.room_name = room_name
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.guests = []
        self.songs = []
        self.till = 0.00

    def add_song_to_room(self, guest):
        self.songs.append(guest.fave_song[0])

    def check_in(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
        else:
            return f"Sorry, {guest.name} this room is full!"

    def check_out(self, guest):
        self.guests.remove(guest)

    def collect_fee(self, guest):
        if guest.wallet >= self.entry_fee:
            self.till += self.entry_fee
            guest.wallet -= self.entry_fee
        else:
            return "Sorry you don't have enough money"
    
    def remove_song(self, guest):
        self.songs.remove(guest.fave_song[0])

    def open_tab(self, guest, tab):
        guest.tab.append(tab)

    def add_to_tab(self, guest, amount):
        guest.tab[0].bill += amount

    def complete_check_in(self, guest):
        if self.collect_fee(guest) != None:
            return 
        else: 
            self.check_in(guest)