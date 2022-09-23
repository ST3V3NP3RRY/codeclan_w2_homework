class Room:
    def __init__(self, name):
        self.name = name
        self.guests = []
        self.songs = []

    def check_in_guests(self, guest):
        self.guests.append(guest)

    def check_out_guests(self, guest):
        self.guests.remove(guest)

    def add_song_to_room(self, song):
        self.songs.append(song)

    def number_of_guests_in_room(self, guest):
        room_capacity = 4
        if room_capacity == len(self.guests):
            return room_capacity
        else:
            self.check_in_guests(guest)
