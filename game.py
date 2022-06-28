"""
Created by: Tony Foster
Date: 12/28/2021
Purpose: Fun project to explore data modeling and event driven logic
License: The code in here is considered free for open source projects
"""

#from character import Character
from player import Player
from helper import validate_user_option_and_set_current
from game_reference_data import Game_Ref

game_ref = Game_Ref() #static game data
user = Player()
locations = game_ref.locations
user.valid_locations = locations.keys()

def print_location_options(options):
    for i in range(len(options)):
        print (f"{i+1}. {options[i]}")

game_options = ['help', 'look', 'menu', 'stats', 'inventory', ]#"*"]
def handle_game_option(user_input):
    if user_input == "help":
        print ("Game options:", ", ".join(game_options))
    elif user_input == "look":
        print(locations[user.current_location].long_description)
    elif user_input == "menu":
        current_location_options = locations[user.current_location].options
        print_location_options(current_location_options)
    elif user_input == "stats":
        if user.character:
            user.character.print_stats()
    elif user_input == "inventory":
        print("TODO: List player inventory.")
    #elif user_input == "*":
    #    print("TODO: check back later for additional options.")
    else:
        print("Unknown command error.")

#print(locations)

while user.playing:
    #print location description, menu, get user input, and handle a valid option
    if user.new_location:
        user.new_location = False
        print(locations[user.current_location].long_description)

        location_options = locations[user.current_location].options
        print_location_options(location_options)

    user.input = input("Please select an option: ")
    while not validate_user_option_and_set_current(game_options, location_options, user):
        user.input = input("Please select an option: ")

    if user.current_option in game_options:
        handle_game_option(user.current_option)
    else:
        locations[user.current_location].handler(user, game_ref)
