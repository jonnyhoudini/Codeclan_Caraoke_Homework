import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
from src.tab import Tab

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Lost in Translation", 4, 45.50)
        self.guest = Guest("Bill Murray", 100.00)
        self.guest2 = Guest("Scarlett Johansson", 75.00)
        self.guest3 = Guest("Giovanni Ribisi", 75.00)
        self.guest4 = Guest("Anna Faris", 80.00)
        self.guest5 = Guest("Akiko Takeshita", 75.00)
        self.song = Song("More Than This", "Roxy Music")
        self.tab = Tab("Bill Murray")

    def test_if_room_has_name_capacity_and_entry_fee(self):
        self.assertEqual("Lost in Translation", self.room.room_name)
        self.assertEqual(4, self.room.capacity)
        self.assertEqual(45.50, self.room.entry_fee)
    
    def test_check_that_we_can_check_in_guest(self):
        self.room.check_in(self.guest)
        self.assertEqual("Bill Murray", self.room.guests[0].name)

    def test_we_can_check_out_guest(self):
        self.room.check_in(self.guest)
        self.room.check_out(self.guest)
        self.assertEqual(0, len(self.room.guests))

    def test_we_can_add_songs_to_rooms(self):
        self.guest.add_song(self.song)
        self.room.add_song_to_room(self.guest)
        self.assertEqual(1, len(self.room.songs))

    def test_collect_entry_fee(self):
        self.room.collect_fee(self.guest)
        self.assertEqual(45.50, self.room.till)
        self.assertEqual(54.50, self.guest.wallet)

    def test_collect_entry_fee_guest_is_skint(self):
        self.guest.wallet = 35.00
        self.room.collect_fee(self.guest)
        self.assertEqual(0, self.room.till)
        self.assertEqual("Sorry you don't have enough money", self.room.collect_fee(self.guest))

    def test_check_in_over_capacity(self):
        self.room.check_in(self.guest)
        self.room.check_in(self.guest2)
        self.room.check_in(self.guest3)
        self.room.check_in(self.guest4)
        self.assertEqual(4, len(self.room.guests))
        self.assertEqual(f"Sorry, {self.guest5.name} this room is full!", self.room.check_in(self.guest5))

    def test_remove_song_from_room_at_check_out(self):
        self.guest.add_song(self.song)
        self.room.check_in(self.guest)
        self.room.add_song_to_room(self.guest)
        self.room.check_out(self.guest)
        self.room.remove_song(self.guest)
        self.assertEqual(0, len(self.room.songs))

    def test_open_tab_and_attach_it_to_customer(self):
        self.room.open_tab(self.guest, self.tab)
        self.assertEqual(1, len(self.guest.tab))

    def test_add_to_tab(self):
        self.room.open_tab(self.guest, self.tab)
        self.room.add_to_tab(self.guest, 25)
        self.assertEqual(25, self.guest.tab[0].bill)

    def test_one_function_to_do_the_whole_check_in_process(self):
        self.guest.fave_song = self.song
        self.room.complete_check_in(self.guest)
        self.assertEqual(1, len(self.room.guests))
        self.assertEqual(54.50, self.guest.wallet)
        self.assertEqual(45.50, self.room.till)

    def test_one_function_to_do_the_whole_check_in_process_not_enough_money(self):
        self.guest.wallet = 10
        self.room.complete_check_in(self.guest)
        self.assertEqual(0, len(self.room.guests))
        self.assertEqual(10, self.guest.wallet)
        self.assertEqual(0, self.room.till)