import unittest
from classes.guest import Guest


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Olivia Wilde", 25)

    def test_guest_has_name(self):
        self.assertEqual("Olivia Wilde", self.guest.name)

    def test_guest_has_money(self):
        self.assertEqual(25, self.guest.money)

    def test_find_guest_by_name__name_found(self):
        room_guest = Guest("Mike Mckenzie", 30)
        self.guest.find_guest_by_name(room_guest.name)
        self.assertEqual(room_guest.name, "Mike Mckenzie")

    def test_find_guest_by_name__name_not_found(self):
        room_guest = Guest("Mike Mckenzie", 30)
        self.guest.find_guest_by_name(room_guest)
        result = self.guest.find_guest_by_name("Joe Horner")
        self.assertEqual(None, result)
