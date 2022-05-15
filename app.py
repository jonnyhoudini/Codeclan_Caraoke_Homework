from src.guest import *
from src.room import *
from src.song import *
from src.tab import *

print("Welcome to the CodeClan Caraoke!")
room_name = input("What is the name of the karaoke room? ")
room_capacity = input("What is the capacity of the room? ")
room_entry_fee = input("What is the entry fee? ")

my_room = Room(room_name, int(room_capacity), int(room_entry_fee))

print(f"I have created a room called {room_name}")

guest_name = input("What is the name of the guest? ")
guest_wallet = input("How much money does the guest have? ")

song_title = input("What is the title of the guest's favourite song? ")
song_artist = input("What is the name of the artist? ")

fave_song = Song(song_title, song_artist)
my_guest = Guest(guest_name, int(guest_wallet))

my_guest.add_song(fave_song)
my_room.complete_check_in(my_guest)
my_room.add_song_to_room(my_guest)

print(f"Your guest is called {my_guest.name}")
print(f"They have {my_guest.wallet} left in their wallet")
print(f"The next song to play is {my_room.songs[0].title}")