#from character import Character

class Player():
    def __init__(self):
        self.input = ""
        self.character = None
        self.playing = True
        self.new_location = True
        self.current_location = "Title Screen"
        self.current_option = None
        self.valid_locations = []
        self.in_combat = False

    def change_location(self, location):
        if location in self.valid_locations:
            #print("Moving to:", location)
            self.current_location = location
            self.new_location = True
        else:
            print("Invalid location:", location)

    def print_info(self):
        print(self.input)
        print(self.current_location)
