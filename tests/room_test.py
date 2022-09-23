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

    def test_room_has_name(self):
        self.assertEqual("Rock Room", self.room.name)

    # def test_check_num_of_guests_in_room_starts_at_0(self):
    #     self.assertEqual([], self.room.guests)

    def test_check_in_guests_to_room(self):
        self.room.check_in_guests(self.guest)
        self.assertEqual([self.guest], self.room.guests)

    def test_check_out_guests_from_room(self):
        self.room.check_in_guests(self.guest)
        self.room.check_out_guests(self.guest)
        self.assertEqual([], self.room.guests)

    def test_can_add_song_to_room(self):
        song = Song("Sweet Dreams (Are Made Of This", "Eurythmics", "Alternative")
        self.room.add_song_to_room(song)
        self.assertEqual([song], self.room.songs)

    def test_check_number_of_guests_in_room(self):
        self.room.check_in_guests(self.guest)
        self.room.check_in_guests(self.guest1)
        self.room.check_in_guests(self.guest2)
        # self.room.check_in_guests(self.guest3)
        # Guests are checked in room.guests == 4
        guests = len(self.room.guests)
        self.room.number_of_guests_in_room(self)
        self.assertEqual(4, guests)

        # Check the ho many guests are in the room.

        # if the number of guests == value stored in max_capacity
