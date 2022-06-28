class Enemy():
    def __init__(self, name="NONAME"):
        self.name = name
        self.description = "Temp Description to be overwritten."
        self.max_hp = 0
        self.hp = 0
        self.endurance = 0
        self.attack = 0
        self.defense = 0
        self.stats = [1,1,1,1]
        self.attack_pattern = [100]