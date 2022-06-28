from location import Location
from title_screen import handle_title_screen
from inn import handle_inn
from arena import handle_arena
from combat import handle_combat

def build_locations():
    locations = {}

    title_screen = Location("Title Screen")
    title_screen.long_description = "\
    Welcome to A Short Adventure Game\n\
    Use the help command for additional game options\n\
    "
    title_screen.options = ["Start New Game", "Load Saved Game", "Exit"]
    title_screen.handler = handle_title_screen

    location_inn = Location("Inn")
    location_inn.long_description = "\
    Welcome to the inn\n\
    "
    location_inn.options = ["Retire to room", "Approach dice game", "Go to Arena"]
    location_inn.handler = handle_inn

    location_arena = Location("Arena")
    location_arena.long_description = "\
    Welcome to the Arena\n\
    "
    location_arena.options = ["Sign up to fight", "Go to Inn"]
    location_arena.handler = handle_arena

    location_combat = Location("Combat")
    location_combat.long_description = "\
    The battle has started!\n\
    "
    location_combat.options = ["Attack", "Parry", "Dodge", "Evade"]
    location_combat.handler = handle_combat


    locations[title_screen.name] = title_screen
    locations[location_inn.name] = location_inn
    locations[location_arena.name] = location_arena
    locations[location_combat.name] = location_combat

    return locations
