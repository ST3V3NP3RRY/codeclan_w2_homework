import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Rock Room")
        self.guest = Guest("Jim Morrison", 10)
        self.guest1 = Guest("Amy Winehouse", 15)
        self.guest2 = Guest("Mama Cass", 8)
        self.guest3 = Guest("Jimmy Paige", 16)
        self.guest4 = Guest("John Lennon", 12)

    def test_room_has_name(self):  # 1
        self.assertEqual("Rock Room", self.room.name)

    # def test_check_num_of_guests_in_room_starts_at_0(self):
    #     self.assertEqual([], self.room.guests)

    def test_check_in_guests_to_room(self):  # 2
        self.room.check_in_guests(self.guest)
        self.assertEqual([self.guest], self.room.guests)

    def test_check_out_guests_from_room(self):  # 3
        self.room.check_in_guests(self.guest)
        self.room.check_out_guests(self.guest)
        self.assertEqual([], self.room.guests)

    def test_can_add_song_to_room(self):  # 4
        song = Song("Sweet Dreams (Are Made Of This", "Eurythmics", "Alternative")
        self.room.add_song_to_room(song)
        self.assertEqual([song], self.room.songs)

    def test_check_number_of_guests_in_room(self):  # 5
        self.room.check_in_guests(self.guest)
        self.room.check_in_guests(self.guest1)
        self.room.check_in_guests(self.guest2)
        self.room.check_in_guests(self.guest3)
        # Guests are checked in len(room.guests) == 4
        guests = len(self.room.guests)
        self.room.number_of_guests_in_room(self)
        self.assertEqual(4, guests)

    def test_find_song_by_title__song_found(self):  # 6
        song = Song("Welcome to the Jungle", "Guns 'n' Roses", "Rock")
        self.room.add_song_to_room(song)
        result = self.room.find_song_by_title("Welcome to the Jungle")
        self.assertEqual(song, result)

    def test_find_song_by_title__song_not_found(self):  # 7
        song = Song("Welcome to the Jungle", "Guns 'n' Roses", "Rock")
        self.room.add_song_to_room(song)
        result = self.room.find_song_by_title("Back in Black")
        self.assertEqual(None, result)

    def test_guest_can_afford_fee__sufficent_funds(self):  # 8
        guest = self.guest3
        can_afford_fee = self.room.customer_can_afford_fee(guest)
        self.assertEqual(True, can_afford_fee)

    def test_guest_can_afford_fee__insufficent_funds(self):  # 9
        guest = self.guest2
        can_afford_fee = self.room.customer_can_afford_fee(guest)
        self.assertEqual(False, can_afford_fee)

    def test_find_guest_favourite_song__song_found(self):  # 10
        favourite_song = "Black Dog"
        song = Song("Black Dog", "Led Zeppelin", "Rock")
        self.room.is_favourite_song_in_room(favourite_song, song)
        self.assertEqual(
            "Woo Hoo!", self.room.is_favourite_song_in_room(favourite_song, song)
        )

        # Add song to room
        # Add guest to room
        # Add favourite song to guest
        # Check song is in room
        # Check guest is in room
        # Check if song.title == favourite song
        # IF song is in room return Woo Hoo!
        # Needs multiple asserts
