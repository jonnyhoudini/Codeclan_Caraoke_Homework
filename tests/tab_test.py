import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room
from src.tab import Tab

class TestTab(unittest.TestCase):
    def setUp(self):
        self.tab = Tab("Bill Murray")

    def test_tab_exists_and_has_name(self):
        self.assertEqual("Bill Murray", self.tab.name)
