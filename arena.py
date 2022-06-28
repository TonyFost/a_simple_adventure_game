
# ["Sign up to fight", "Go to Inn"]
def handle_arena(player, game_data):
    if player.input == "1":
        if player.character.arena_wins == 0:
            print ("You sign up for your first fight!")
        else:
            print ("Once again you enter the battlefield to test your mettle.")

        print("You enter the arena, waiting for your opponent. From the other side you see the gate open.")
        print(game_data.enemies[player.character.arena_wins].description)
        
        player.change_location("Combat")
    elif player.input == "2":
        print ("You seek the comforts of the inn.")
        player.change_location("Inn")