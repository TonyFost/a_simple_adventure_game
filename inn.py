
#["Retire to room", "Approach dice game", "Go to Arena"]
def handle_inn(player, game_data):
    if player.input == "1":
        print ("You retire to your room to wash off the grime of the day.")
        player.character.hp = player.character.max_hp
        print("Restored HP:",player.character.hp)
    elif player.input == "2":
        print ("The men playing dice snarl at you and tell you to get lost.")
    elif player.input == "3":
        player.change_location("Arena")
