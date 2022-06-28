from enemy import Enemy

def build_enemies():
    enemies = []

    enemy0 = Enemy("Scrawny Fighter")
    enemy0.max_hp = enemy0.hp = 8
    enemy0.attack = 1
    enemy0.defense = 0
    enemy0.stats = [1,1,2,2]
    enemy0.endurance = enemy0.stats[2]*5
    enemy0.attack_pattern = [70,10,10,10]
    enemy0.description = "A malnourished man wanders through the gate. You wonder if he's lost, but best not ask questions here."

    enemy1 = Enemy("Vagabond")
    enemy1.max_hp = enemy1.hp = 12
    enemy1.attack = 2
    enemy1.defense = 2
    enemy1.stats = [2,2,2,2]
    enemy1.endurance = enemy1.stats[2]*5
    enemy1.attack_pattern = [30,30,30,10]
    enemy1.description = "A rough looking man enters with a sword in hand. You hope he puts up more of a fight than the last guy."

    enemy2 = Enemy("Cutthroat")
    enemy2.max_hp = enemy2.hp = 14
    enemy2.attack = 3
    enemy2.defense = 1
    enemy2.stats = [1,3,1,3]
    enemy2.endurance = enemy2.stats[2]*5
    enemy2.attack_pattern = [20,40,40,0]
    enemy2.description = "A wiry looking man with a dagger enters. He has an evil glint in his eye."

    enemy3 = Enemy("Pugilist")
    enemy3.max_hp = enemy3.hp = 16
    enemy3.attack = 2
    enemy3.defense = 3
    enemy3.stats = [1,4,3,3]
    enemy3.endurance = enemy3.stats[2]*5
    enemy3.attack_pattern = [50,0,40,10]
    enemy3.description = "This man isn't weilding a weapon, but to have made it this far he must be tough."

    enemy4 = Enemy("Disgraced Armored Knight")
    enemy4.max_hp = enemy4.hp = 20
    enemy4.attack = 5
    enemy4.defense = 5
    enemy4.stats = [4,2,3,1]
    enemy4.endurance = enemy4.stats[2]*5
    enemy4.attack_pattern = [50,50,0,0]
    enemy4.description = "A heavily armored knight enters. The sun shines brightly off his polished full plate."

    enemy5 = Enemy("Duelist")
    enemy5.max_hp = enemy5.hp = 20
    enemy5.attack = 4
    enemy5.defense = 2
    enemy5.stats = [2,5,3,4]
    enemy5.endurance = enemy5.stats[2]*5
    enemy5.attack_pattern = [10,70,10,10]
    enemy5.description = "A woman enters carrying a long pointy sword. You're not sure of the name, but this foe should not be underestimated."

    enemy6 = Enemy("Towering Strongman")
    enemy6.max_hp = enemy6.hp = 40
    enemy6.attack = 8
    enemy6.defense = 6
    enemy6.stats = [7,3,5,3]
    enemy6.endurance = enemy6.stats[2]*5
    enemy6.attack_pattern = [100,0,0,0]
    enemy6.description = "A hulking towering being enters with a giant double-headed axe. Going head-to-head will be painful."

    enemy7 = Enemy("Assassin")
    enemy7.max_hp = enemy7.hp = 24
    enemy7.attack = 6
    enemy7.defense = 4
    enemy7.stats = [3,5,4,6]
    enemy7.endurance = enemy7.stats[2]*5
    enemy7.attack_pattern = [30,30,40,0]
    enemy7.description = "The gate opens, but you don't see anyone enter. As you turn to leave you feel a presence approach. Ready yourself!"

    enemy8 = Enemy("Trickster")
    enemy8.max_hp = enemy8.hp = 12
    enemy8.attack = 2
    enemy8.defense = 4
    enemy8.stats = [2,8,8,10]
    enemy8.endurance = enemy8.stats[2]*5
    enemy8.attack_pattern = [0,10,10,80]
    enemy8.description = "Looks like the court jester got thrown into the arena. This should be an easy bout, Right?"

    enemy9 = Enemy("Arena Champion")
    enemy9.max_hp = enemy9.hp = 50
    enemy9.attack = 20
    enemy9.defense = 20
    enemy9.stats = [9,9,9,9]
    enemy9.endurance = enemy9.stats[2]*5
    enemy9.attack_pattern = [40,30,20,10]
    enemy9.description = "Finally, the time has arrived to challenge the last fighter. Prepare yourself for the hardest battle!"

    enemies.append(enemy0)
    enemies.append(enemy1)
    enemies.append(enemy2)
    enemies.append(enemy3)
    enemies.append(enemy4)
    enemies.append(enemy5)
    enemies.append(enemy6)
    enemies.append(enemy7)
    enemies.append(enemy8)
    enemies.append(enemy9)

    return enemies
