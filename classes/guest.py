class Guest:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        

    def find_guest_by_name(self, guest_name):
        if self.name == guest_name:
            return guest_name
