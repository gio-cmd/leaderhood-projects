def print_message(message):
    print(message)
    print(" ")

def get_input(prompt):
    return input(prompt).strip().lower()

def check_input(user_input, options):
    if user_input in options:
        return True
    print("Choose the right option!")
    quit()

def game_over(points):
    print(f"Your points: {points}")
    print("Game Over")
    quit()

def run_adventure():
    points = 0
    player_name = input("Enter your name: ")

    print_message("Welcome to the Adventure Game!")
    print_message(f"Hello {player_name}, let's begin your adventure!")

    run_or_fight = get_input("Run or Fight? (r/fight): ")
    check_input(run_or_fight, ["r", "fight"])

    if run_or_fight == "r":
        points -= 3
        print_message("You got away but Lukas is not lucky enough.")
        print_message("A decade passed.")
        print_message("You feel bad for leaving Lukas alone and now want to avenge him.")
        print_message("In the search for the dragon, you became a hitman. On one unsuspecting normal day, you accidentally found the dragon.")
        points += 8
        sneaky_attack = get_input("Dragon doesn't seem to see you. Attack him: (c/j): ")
        check_input(sneaky_attack, ["c", "j"])

        if sneaky_attack == "c":
            print_message("Dragon saw you and dodged your attack.")
        elif sneaky_attack == "j":
            print_message("Dragon saw that jab coming and blocked it.")
        
        print_message("It seems like the difference between you and the dragon is too much.")
        print_message("It will be hard to defeat the dragon since you couldn't even hit him once.")
        plan = get_input("How do you plan on defeating it: ")
        print_message("That might work.")

        block_or_dodge = get_input("Dragon is charging a fireball attack. Try to negate the damage: (d/b): ")
        check_input(block_or_dodge, ["d", "b"])

        if block_or_dodge == "d":
            print_message("You dodged it.")
        elif block_or_dodge == "b":
            print_message("You got burned alive.")
            quit()

        print_message("Now it is your time to attack.")
        attack = get_input("Type the attack: ")
        print_message("Your attacks start to cause some damage. You are getting better at this.")
        
        killer_move = get_input("Dragon is using Azura Breath. It usually is the killer move. Dodge it!! (d/b): ")
        check_input(killer_move, ["d", "b"])

        if killer_move == "d":
            print_message("You tried to dodge it but the attack still grazed you. You are at 3% health.")
        elif killer_move == "b":
            print_message("You blocked but you are left with 1% health.")
        else:
            print_message("You died.")
            quit()

        print_message("New skill activated: When you have HP lower or equal to 3%, you can use 'ATOMIC BREATH'.")
        final_blow = get_input("Use your new learned ability to finish the dragon (a): ")
        check_input(final_blow, ["a"])

        if final_blow == "a":
            print_message("Dragon is finished.")
            print_message("You unlocked a new title: 'Dragon Killer'.")
            if " (The Honored One)" in player_name:
                player_name = player_name.replace(" (The Honored One)", " (Dragon Killer)")
            else:
                player_name += " (Dragon Killer)"
        else:
            print_message("Please use your new learned ability.")
            quit()
    else:
        print_message("Choose the right option!")
        quit()

    print_message(f"{player_name}: That was something unimaginable, right?")
    print_message("Lukas: I can't disagree about that.")
    print_message("You faint from exhaustion.")
    game_over(points)

