import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Bill Murray", 100.00)
        self.song = Song("More Than This", "Roxy Music")
        self.room = Room("Lost in Translation", 5, 45.50)

    def test_guest_has_name_and_wallet(self):
        self.assertEqual("Bill Murray", self.guest.name)
        self.assertEqual(100.00, self.guest.wallet)

    def test_can_add_song_to_guest(self):
        self.guest.add_song(self.song)
        self.assertEqual(1, len(self.guest.fave_song))
        self.assertEqual("More Than This", self.guest.fave_song[0].title)

    def test_cheer_fave_song(self):
        self.guest.add_song(self.song)
        self.room.check_in(self.guest)
        self.room.add_song_to_room(self.guest)
        self.assertEqual("CHOOOON!", self.guest.cheer_loudly(self.room))
