import random

#["Attack", "Parry", "Dodge", "Evade"]
def handle_combat(player, game_data):
    enemy = game_data.enemies[player.character.arena_wins]

    enemy_stance = random.randint(1,100)
    enemy_option = 0
    while enemy_stance > 0:
        enemy_stance -= enemy.attack_pattern[enemy_option]
        enemy_option += 1

    player_damage = max(0, (player.character.attack if player.character.endurance > 0 else player.character.attack // 2) - enemy.defense)
    enemy_damage = max(0, (enemy.attack if enemy.endurance > 0 else enemy.attack // 2) - player.character.defense)
    crit = 1

    if player.input == "1":
        player_damage += player.character.stats[0] + (4*(player.character.stats[0]//5)) #add strength to attack
        #print(player_damage)
        #print(player.character.endurance)
        player.character.endurance -= 2

        if enemy_option == 1:
            enemy.endurance -= 1
            #both attack
            enemy_damage += enemy.stats[0] + (3*(enemy.stats[0]//5)) #add strength to attack
            print("You both exchange blows!")

        if enemy_option == 2:
            #player attacks, enemy parries
            enemy.endurance -= 1
            dex_diff = player.character.stats[1] / enemy.stats[1]
            if enemy.stats[1] > player.character.stats[1] and random.randint(1,6) != 1:
                player.character.endurance -= 1
                player_damage = max(0, player_damage - (enemy.stats[1] * 2))
                enemy_damage += (enemy.stats[1] // 2)
                print(f"As you charge in, the {enemy.name} deftly glances your blows away with their weapon.")
            else:
                enemy.endurance -= 1
                player_damage += (player.character.stats[0] * dex_diff if dex_diff > 1 else player.character.stats[0] + 2)
                enemy_damage = max(0, enemy_damage - player.character.stats[1])
                print(f"Your attacks overwhelm the {enemy.name} as they try to parry.")

        if enemy_option == 3:
            #player attacks, enemy dodges
            enemy.endurance -= 1
            agl_diff = player.character.stats[3] / enemy.stats[3]
            enemy_damage = enemy_damage // 2
            if enemy.stats[3] > player.character.stats[3] and random.randint(1,6) != 1:
                player.character.endurance -= 2
                player_damage = max(0, player_damage - (enemy.stats[3] * 3))
                enemy_damage += enemy.stats[3]
                print(f"As you charge in, the {enemy.name} deftly dodges your blows.")
            else:
                enemy.endurance -= 2
                player_damage += (player.character.stats[0] * agl_diff  if agl_diff > 1 else player.character.stats[0] + 2)
                enemy_damage = max(0, enemy_damage - player.character.stats[3])
                print(f"You easily strike the {enemy.name} as they attempt to manuever around your attack.")

        if enemy_option == 4:
        #player attacks, enemy evades
            sta_diff = player.character.stats[2] / enemy.stats[2]
            enemy_damage = 0
            if enemy.stats[2] > player.character.stats[2] and random.randint(1,6) != 1:
                player.character.endurance -= 4
                enemy.endurance += 1
                if (enemy.stats[3] + random.randint(1,6)) > (player.character.stats[3] + random.randint(1,6)):
                    player_damage = 0
                    enemy_damage = 1
                    print(f"As you charge in, the {enemy.name} completely evades your blows.")
                else:
                    player_damage = player_damage // enemy.stats[3]
                    print(f"Your attack lands, but the {enemy.name} avoids the brunt of it.")
            else:
                enemy.endurance = (enemy.endurance // sta_diff if sta_diff > 1 else enemy.endurance - player.character.stats[2])
                player_damage += player.character.stats[0]
                crit = 2
                print(f"You strike a heavy blow against the {enemy.name} as they attempt to avoid your attack.")

    if player.input == "2":
        player.character.endurance -= 1

        if enemy_option == 1:
            enemy.endurance -= 1
            #both attack
            enemy_damage += enemy.stats[0] + (3*(enemy.stats[0]//5)) #add strength to attack
            print(f"The {enemy.name} charges at you with a strong attack!")

        if enemy_option == 2:
            #player attacks, enemy parries
            enemy.endurance -=1
            dex_diff = player.character.stats[1] / enemy.stats[1]
            if enemy.stats[1] > player.character.stats[1] and random.randint(1,6) != 1:
                player.character.endurance -= 1
                player_damage = max(0, player_damage - (enemy.stats[1] * 2))
                enemy_damage += (enemy.stats[1] // 2)
                print(f"The {enemy.name} prepares to meet your attack.")
            else:
                enemy.endurance -= 1
                player_damage += (player.character.stats[0] * dex_diff if dex_diff > 1 else player.character.stats[0] + 2)
                enemy_damage = max(0, enemy_damage - player.character.stats[1])
                print(f"The {enemy.name} readies their weapon, but you take advantage of a weakness in their stance.")

        if enemy_option == 3:
            #player attacks, enemy dodges
            enemy.endurance -= 1
            agl_diff = player.character.stats[3] / enemy.stats[3]
            enemy_damage = enemy_damage // 2
            if enemy.stats[3] > player.character.stats[3] and random.randint(1,6) != 1:
                player.character.endurance -= 2
                player_damage = max(0, player_damage - (enemy.stats[3] * 3))
                enemy_damage += enemy.stats[3]
                print(f"The {enemy.name} deftly weaves through your stance.")
            else:
                enemy.endurance -= 2
                player_damage += (player.character.stats[0] * agl_diff if agl_diff > 1 else player.character.stats[0] + 2)
                enemy_damage = max(0, enemy_damage - player.character.stats[3])
                print(f"The {enemy.name} trips overthemselves rolling around, almost tumbling into you.")

        if enemy_option == 4:
        #player attacks, enemy evades
            sta_diff = player.character.stats[2] / enemy.stats[2]
            enemy_damage = 0
            if enemy.stats[2] > player.character.stats[2] and random.randint(1,6) != 1:
                player.character.endurance -= 4
                enemy.endurance += 1
                if (enemy.stats[3] + random.randint(1,6)) > (player.character.stats[3] + random.randint(1,6)):
                    player_damage = 0
                    enemy_damage = 1
                    print(f"The {enemy.name} keeps their distance taking potshots at you with small pebbles.")
                else:
                    player_damage = player_damage // enemy.stats[3]
                    print(f"As the {enemy.name} avoids you, you're able to land only glancing blows.")
            else:
                enemy.endurance = (enemy.endurance // sta_diff if sta_diff > 1 else enemy.endurance - player.character.stats[2])
                player_damage += player.character.stats[0]
                crit = 2
                print(f"You prepare to meet the {enemy.name}'s attack as they fall head first into you!")

        dex_diff = enemy.stats[1] / player.character.stats[1]
        if player.character.stats[1] > enemy.stats[1] or random.randint(1,6) > 4:
            enemy.endurance -= 1
            enemy_damage = (enemy_damage * dex_diff if dex_diff < 1 else max(0, enemy_damage - player.character.stats[1]))
            player_damage += (player.character.stats[1] // 2)
            print(f"You've successfully met the {enemy.name}'s attack.")
        else:
            player.character.endurance -= 1
            enemy_damage += (enemy.stats[0] * dex_diff if dex_diff > 1 else enemy.stats[0] // 2)
            player_damage = max(0, player_damage - enemy.stats[1])
            print(f"You falter in your stance against the {enemy.name}.")

    if player.input == "3":

        if enemy_option == 1:
            enemy.endurance -= 1
            #both attack
            enemy_damage += enemy.stats[0] + (3*(enemy.stats[0]//5)) #add strength to attack
            print(f"The {enemy.name} charges at you with a strong attack!")

        if enemy_option == 2:
            #player attacks, enemy parries
            enemy.endurance -=1
            dex_diff = player.character.stats[1] / enemy.stats[1]
            if enemy.stats[1] > player.character.stats[1] and random.randint(1,6) != 1:
                player.character.endurance -= 1
                player_damage = max(0, player_damage - (enemy.stats[1] * 2))
                enemy_damage += (enemy.stats[1] // 2)
                print(f"The {enemy.name} prepares to meet your attack.")
            else:
                enemy.endurance -= 1
                player_damage += (player.character.stats[0] * dex_diff if dex_diff > 1 else player.character.stats[0] + 2)
                enemy_damage = max(0, enemy_damage - player.character.stats[1])
                print(f"The {enemy.name} readies their weapon, but you see an opening in their stance.")

        if enemy_option == 3:
            #player attacks, enemy dodges
            enemy.endurance -= 1
            agl_diff = player.character.stats[3] / enemy.stats[3]
            enemy_damage = enemy_damage // 2
            if enemy.stats[3] > player.character.stats[3] and random.randint(1,6) != 1:
                player.character.endurance -= 2
                player_damage = max(0, player_damage - (enemy.stats[3] * 3))
                enemy_damage += enemy.stats[3]
                print(f"The {enemy.name} deftly weaves through your movements.")
            else:
                enemy.endurance -= 2
                player_damage += (player.character.stats[0] * agl_diff if agl_diff > 1 else player.character.stats[0] + 2)
                enemy_damage = max(0, enemy_damage - player.character.stats[3])
                print(f"The {enemy.name} trips over themselves rolling around, almost tumbling into you!")

        if enemy_option == 4:
        #player attacks, enemy evades
            sta_diff = player.character.stats[2] / enemy.stats[2]
            enemy_damage = 0
            if enemy.stats[2] > player.character.stats[2] and random.randint(1,6) != 1:
                player.character.endurance -= 4
                enemy.endurance += 1
                if (enemy.stats[3] + random.randint(1,6)) > (player.character.stats[3] + random.randint(1,6)):
                    player_damage = 0
                    enemy_damage = 1
                    print(f"The {enemy.name} keeps their distance taking potshots at you with small pebbles.")
                else:
                    player_damage = player_damage // enemy.stats[3]
                    print(f"As the {enemy.name} avoids you, you're able to land only glancing blows.")
            else:
                enemy.endurance = (enemy.endurance // sta_diff if sta_diff > 1 else enemy.endurance - player.character.stats[2])
                player_damage += player.character.stats[0]
                crit = 2
                print(f"You prepare to dodge the {enemy.name}'s attack as they fall head first into you!")

        agl_diff = player.character.stats[3] / enemy.stats[3]
        player_damage = player_damage // 2
        if player.character.stats[3] > enemy.stats[3] or random.randint(1,6) > 4:
            enemy.endurance -= 2
            enemy_damage = (enemy_damage * agl_diff * agl_diff if agl_diff < 1 else max(0, enemy_damage - player.character.stats[3]))
            player_damage += (player.character.stats[3] )
            print(f"You weave around the {enemy.name}'s attack, striking when opportunity rises.")
        else:
            player.character.endurance -= 1
            enemy_damage += (enemy.stats[0] * agl_diff * agl_diff if agl_diff > 1 else enemy.stats[0] // 2)
            player_damage = max(0, player_damage - enemy.stats[3])
            print(f"You misstep several times, and the {enemy.name} takes advantage.")

    if player.input == "4":
        player.character.endurance += 1
        player_damage = 0

        if enemy_option == 1:
            enemy.endurance -= 1
            #both attack
            enemy_damage += enemy.stats[0] + (3*(enemy.stats[0]//5)) #add strength to attack
            print(f"The {enemy.name} charges at you with a strong attack!")

        if enemy_option == 2:
            #player attacks, enemy parries
            enemy.endurance -=1
            dex_diff = player.character.stats[1] / enemy.stats[1]
            if enemy.stats[1] > player.character.stats[1] and random.randint(1,6) != 1:
                player.character.endurance -= 1
                enemy_damage += enemy.stats[1]
                print(f"The {enemy.name} meets your retreat.")
            else:
                enemy.endurance -= 1
                player.character.endurance += 1
                enemy_damage = max(0, enemy_damage - player.character.stats[1])
                print(f"The {enemy.name} readies their weapon, but fails to see your retreat.")

        if enemy_option == 3:
            #player attacks, enemy dodges
            enemy.endurance -= 1
            enemy_damage = enemy_damage // 2
            if enemy.stats[3] > player.character.stats[3] and random.randint(1,6) != 1:
                player.character.endurance -= 2
                enemy_damage += enemy.stats[3]*2
                print(f"The {enemy.name} keeps you on your toes.")
            else:
                enemy.endurance -= 2
                enemy_damage = max(0, enemy_damage - player.character.stats[3])
                print(f"The {enemy.name} flails wildly as you attempt to retreat.")

        if enemy_option == 4:
        #player attacks, enemy evades
            enemy_damage = 0
            if enemy.stats[2] > player.character.stats[2] and random.randint(1,6) != 1:
                enemy.endurance += 2
                if (enemy.stats[3] + random.randint(1,6)) > (player.character.stats[3] + random.randint(1,6)):
                    print(f"The {enemy.name} ran to the opposite end of the arena.")
            else:
                player_damage += 1
                crit = 2
                print(f"The {enemy.name} falls down several times scrambling to the other side of the arena.")

        sta_diff = player.character.stats[2] / enemy.stats[2]
        if player.character.stats[2] > enemy.stats[2] or random.randint(1,6) > 5:
            enemy.endurance -= 4
            player.character.endurance += 2
            if (player.character.stats[3] + random.randint(1,6)) > (enemy.stats[3] + random.randint(1,3)):
                player.character.hp = min(player.character.max_hp, player.character.hp+2)
                enemy_damage = 0
                player_damage += 1
                print(f"You evade the {enemy.name} while throwing small pebbles and tending to your wounds as time allows.")
            else:
                enemy_damage = enemy_damage // player.characrer.stats[3]
                print(f"The {enemy.name} does minimal damage as you excute your evasion tactics.")
        else:
            player.character.endurance = player.character.endurance - enemy.stats[2]
            if not enemy_option == 4:
                enemy_damage += enemy.stats[0]
            print(f"You turn to flee, leaving yourself wide open to the {enemy.name}'s attack.")

    #print(player_damage, enemy_damage)
    #enemy_hitrate = enemy.stats[1] - player.character.stats[3]
    #player_hitrate = player.character.stats[1] - enemy.stats[3]

    enemy_damage = enemy_damage * ((enemy.stats[3] // 5)+1)
    player_damage = player_damage * ((player.character.stats[3] // 5)+1)
    total_enemy_damage = int(enemy_damage )

    total_player_damage = int( (player_damage *crit))

    #print(total_player_damage, total_enemy_damage, player_damage, enemy_damage)#, player_hitrate, enemy_hitrate)
    print(f"{player.character.name} did {total_player_damage} to the {enemy.name}.")
    enemy.hp -= total_player_damage

    if enemy.hp <= 0:
        if player.character.arena_wins == 9:
            print("You've won!")
            print(f"{player.character.name} is the new arena champion!")
            print("Feel free to start a new game~!")
            player.change_location("Title Screen")
        else:
            print("You've won the battle and leave victorious!")
            player.character.arena_wins += 1
            player.character.level_up()
            print("Return once you're ready for the next challenge.")
            player.change_location("Arena")
    else:
        player.character.hp -= total_enemy_damage
        print(f"{player.character.name} took {total_enemy_damage} damage and has {player.character.hp} hit points left.")

        if player.character.hp <= 0:
            print(f"The {enemy.name} overwhelmed you.")
            print("You've been carried back to your room to try again another day.")
            enemy.hp = enemy.max_hp
            player.change_location("Inn")
