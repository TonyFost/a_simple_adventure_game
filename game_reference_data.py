from enemy_data import build_enemies
from game_locations import build_locations

class Game_Ref():
    def __init__(self):
        self.locations = build_locations()
        self.enemies = build_enemies()