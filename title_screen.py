#from player import Player
from character import Character

def new_game():
    print("Creating name character.")
    new_player = Character()
    new_player.name = input("Enter your character's name: ")
    CREATE_CHARACTER = True

    while CREATE_CHARACTER:
        print("Character name:", new_player.name)
        print("Select primary and secondary combat focus")
        print("1. Strength - physical prowess")
        print("2. Dexterity - ability to move with precision")
        print("3. Stamina - physical endurance")
        print("4. Agility - ability to move quickly")
        
        primary = input("Select primary attribute by number: ")
        secondary = input("Select secondary attribute by number: ")
        
        if primary == secondary:
            print("Please select two different options.\n")
            continue
        else:
            try:
                i_primary = int(primary)
                i_secondary = int(secondary)

                if i_primary >=1 and i_primary <= len(new_player.stats) and i_secondary >=1 and i_secondary <= len(new_player.stats):
                    new_player.change_stat(i_primary-1, 2)
                    new_player.change_stat(i_secondary-1, 1)
                    new_player.update_attributes()
                    new_player.hp = new_player.max_hp
                    CREATE_CHARACTER = False
                else:
                    print ("Invalid option was selected. Try again.\n")
            except:
                print("Please enter only numbers.\n")
                continue
    
    return new_player

# ["Start New Game", "Load Saved Game", "Exit"]
def handle_title_screen(player, game_data):
    if player.input == "1":
        player.character = new_game()
        player.character.print_stats()
        player.change_location("Inn")

    elif player.input == "2":
        print("TODO: Implement save and load system")

    else:
        print("You've chosen to exit. Goodbye")
        player.playing = False
