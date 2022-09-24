import unittest
from classes.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Born to Run", "Bruce Springsteen", "Rock")

    def test_song_has_title(self):  # 1
        self.assertEqual("Born to Run", self.song1.title)

    def test_song_has_artist(self):  # 2
        self.assertEqual("Bruce Springsteen", self.song1.artist)

    def test_song_has_genre(self):  # 3
        self.assertEqual("Rock", self.song1.genre)
