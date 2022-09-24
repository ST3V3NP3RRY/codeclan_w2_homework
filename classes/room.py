class Room:
    def __init__(self, name):
        self.name = name
        self.guests = []
        self.songs = []
        self.entrance_fee = 10

    # How can I populate the songs with a list of song objects to start with?
    def check_in_guests(self, guest):
        self.guests.append(guest)

    def check_out_guests(self, guest):
        self.guests.remove(guest)

    def guests_in_room(self):
        return self.guests

    def add_song_to_room(self, song):
        self.songs.append(song)

    def find_song_by_title(self, title):
        for song in self.songs:
            if song.title == title:
                return song

    def customer_can_afford_fee(self, guest):
        return guest.money >= self.entrance_fee

    def is_guest_favourite_song_in_room(self, favourite_song, song):
        if favourite_song == song.title:
            return "Woo Hoo!"

    def check_room_capacity(self, capacity, guest):
        if capacity == len(self.guests):
            return "Room Full"
        if capacity != len(self.guests):
            # self.check_in_guests(guest)
            return "Access granted"

        # Can you add a guest inside this function and still have the test say "Access granted."

        # num_of_guests = len(self.guests)
        # if num_of_guests == capacity:
        #     return "Room Full"
        # else:
        #     return "Access granted"
