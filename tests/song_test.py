import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("More Than This", "Roxy Music")

    def test_song_has_title_and_artist(self):
        self.assertEqual("More Than This", self.song.title)
        self.assertEqual("Roxy Music", self.song.artist)

