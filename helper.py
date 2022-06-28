
def validate_user_option_and_set_current(game_options, location_options, user):
    """Validates game options with a list of menu options at the end against a user.input and assigns the option to current_option"""
    #print(game_options + location_options)
    #get number of options in the menu 

    menu_options_num = len(location_options)
    valid_menu_options = []
    
    for i in range(menu_options_num):
        valid_menu_options.append(str(i+1))

    if user.input == "":
        print("Sorry, I didn't quite get that.")

    #single character input
    if user.input.isdigit():
        if user.input in valid_menu_options:
            user.current_option = int(user.input)
            return True #valid menu option
        else:
            print("Menu choice not listed.")
    else:
        for o in game_options:
            if user.input.lower() == o or user.input.lower() == o[0] or user.input[0] == game_options[-1]: #TODO: improve later by accepting short versions of commands between length 2 and legnth of command
                user.current_option = o
                return True #found a valid game option
        print("I don't understand that option. Use help for a list of commands.")
        
    return False

