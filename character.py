class Character:
    def __init__(self):
        self.name = ""
        self.stats = [1,1,1,1]
        self.weapon = 1
        self.armor = 1
        self.gold = 0
        self.arena_wins = 0
        self.max_hp = 10
        self.hp = 10
        self.endurance = 5
        self.attack = 1
        self.defense = 1

    def change_stat(self, stat, num):
        if stat == "str" or stat == 0:
            self.stats[0] += num
        elif stat == "dex" or stat == 1:
            self.stats[1] += num
        elif stat == "sta" or stat == 2:
            self.stats[2] += num
        elif stat == "agl" or stat == 3:
            self.stats[3] += num

    def update_attributes(self):
        self.max_hp = 10 + self.stats[0] + self.stats[2]
        self.endurance = 5 + (self.stats[2]*5)
        self.attack = self.weapon + self.stats[0]
        self.defense = self.armor + self.stats[3]

    def print_stats(self):
        print(f"Name: {self.name} Current/Max HP: {self.hp}/{self.max_hp} Endurance: {self.endurance} Attack: {self.attack} Defense: {self.defense}")
        print(f"Strength: {self.stats[0]} Dexterity: {self.stats[1]} Stamina: {self.stats[2]} Agility: {self.stats[3]}")

    def level_up(self):
        stat_points = 2
        print("You've leveled up!")
        print(f"You have {stat_points} stat points to assign. Please select an option below:")
        print("1. Strength")
        print("2. Dexterity")
        print("3. Stamina")
        print("4. Agility")
        
        while stat_points > 0:
            if stat_points == 1:
                plural = ""
            else:
                plural = "s"

            stat = input(f"{stat_points} point{plural} left: ")
            if stat.isdigit():
                stat = int(stat)
                if int(stat) > 0 and int(stat) < 5:
                    self.stats[int(stat)-1] += 1
                    stat_points -= 1
                else:
                    print("Please enter a digit between 1 - 4.")
            else:
                print("Please enter a digit between 1 - 4.")
        
        self.update_attributes()
        self.print_stats()
                

