import unittest
from classes.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Born to Run", "Bruce Springsteen", "Rock")

    def test_song_has_title(self):
        self.assertEqual("Born to Run", self.song1.title)

    def test_song_has_artist(self):
        self.assertEqual("Bruce Springsteen", self.song1.artist)

    def test_song_has_genre(self):
        self.assertEqual("Rock", self.song1.genre)
