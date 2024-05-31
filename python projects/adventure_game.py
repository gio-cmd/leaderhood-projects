points = 0# firs origanal game i create. might suck who knows but for exp i try making something
print("Adventure Game")
print(" ")

welcome = input("Hello adventurer! Would you like to take part in this amazing experience? (Yes/No): ")

if welcome.lower() == "yes":
    print("Good choice!")
else:
    quit()

player_name = input("your name: ")

# Ask for the player's experience level
player_experience = input("to better evaluete your gaming experience please choose your rank: Beginner/Novice/Experienced or Expert: ")

# Function to format items with bullet points
def format_with_bullet_point(items):
    for item in items:
        print("\u2022 " + item)  # Using Unicode character for bullet point (U+2022)

# Check the player's experience level and provide bonuses accordingly
if player_experience.lower() == "beginner":
    print("As a beginner, you will be playing on the easiest version of the game with added bonuses:")
    beginner_bonuses = ["Monsters Cannot See You", "You Have Unlimited Respawns", "50% More Regeneration", "2x Experience"]
    print("List of Bonuses:")
    format_with_bullet_point(beginner_bonuses)

elif player_experience.lower() == "novice":
    print("I see you have a bit of experience. Your game experience will be slightly harder but nothing impossible:")
    novice_bonuses = ["Monsters sometimes see you", "You don't have any respawns", "39% More Regeneration", "2x Experience"]
    print("List of Bonuses:")
    format_with_bullet_point(novice_bonuses)

elif player_experience.lower() == "experienced":
    print("As an experienced player, your game experience will be slightly harder. Here's the list of 'bonuses': ")
    experienced_bonuses = ["Monsters always See You", "You don't have any respawns", "No regeneration boost", "1.5x Experience"]
    print("List of Bonuses:")
    format_with_bullet_point(experienced_bonuses)

elif player_experience.lower() == "expert":
    print("This is hardest gamemode be carefull not to loose even though i think you will beat this easily! Here's list of drawbacks: ")
    experienced_bonuses = ["Monsters always know were you are", "You don't have any respawns", "No regeneration", "No experience boost", "If unlucky you can get blinded for 10 seconds"]
    print("List of Drawbacks:")
    format_with_bullet_point(experienced_bonuses)
else:
    print("please choose correct experience level")


print("Let's Begin")
#Beginner level game
if player_experience.lower() == "beginner":
    print("You embarked on a serene camping trip with your family, deep in a dense forest. Amidst the beauty, you stumbled upon enigmatic symbols and strange whispers, eventually losing your way back to the campsite as darkness descended. Alone, you must navigate the unfamiliar woods, solve mysteries, and overcome dangers to reunite with your loved ones. Can you trust your instincts to guide you home?")
    #EXPERIENCE BEGINS!
    strange_voice = (input("Uhh! Whats that voice? Want to check the origins of this voice?: (yes/no)"))
    #If players checks the voice game agains otherwise it ends
    if strange_voice.lower() == "yes":
        print("Did you hear that? Over there look there is someone over there!")
        print("From the shadows emerges guy named lukas. His glowing red eyes lock onto yours. Lukas: You finally came traveller from today onwards you will experience the secrets of this world and you my friend are going to save everyone!")
    elif strange_voice.lower() == "no":
        print("You hide in the bushes till the morning and find your family. You leave forest unharmed with your family")
        quit()
    else:
        print("Choose the right option!")
        quit()

    #New character lukas
    input("Lukas: lets go alredy what are you waiting for: ")
    print(player_name+": Yeah but were are we going?")
    print("Lukas: Well i dunno you choose")

    location = input("Choose the location: ")

    print("Lukas: Okey so were heading to", location)

    first_fight = input("On the way to the " + location + " you encounter a monster. Do you want to fight it alone or get help from Lucas. (alone/with Lukas): ")
    
    experienced_bonuses = ["c = counter attack", "b = block", "d = dodge", "j = jab", "r = run"]
    print("basic attacks:")
    format_with_bullet_point(experienced_bonuses)

    print(" ")
    #First fight + way to gain points 
    if first_fight == "alone":
        points += 12
        move = input("monster is attacking from the left what do you do: (use c/b/d/j) ")
        if move == "d":
            print("Nice you dodged it")
        elif move == "c":
            print("Wow you sure got guts to counter mosnter like that. Your counter did great damage")
        elif move == "b":
            print("You blocked but monster is really strong and it did some damage")
        elif move == "j":
            print("You were too slow monster hit you first")
        input("You have another opportunity to attack, what are you going to do?: ")
        print("I am amazed it only grazed the monster but yet monster got knocked down")
        honor_or_win = input("Attack the monster before it gets up. Do you attack?: (Yes/No)")
        if honor_or_win.lower() == "yes":
            print("Monster has been deleted from existence from your attack. Great Job")
        elif honor_or_win.lower() == "no":
            print("You now have earned a title 'The Honored One'")
            player_name += ' (The Honored One)'
            input("You are out of breath you need to finish this quickly use one final attack before monster attacks back. What do you do: ")
            print("Lukas: Good job that finished it")
        else:
            print("Choose the right option!")
            quit()
        
    elif first_fight.lower() == "with lucas":
        print("You dash and attack the monster a few times but it doesnt seem to harm him")
        print("Lukas: Move out for a moment it's my turn now")
        print("Lukas is on another level he beat monster with single blow")
        points += 7

    elif first_fight.lower() != "with lucas" or "alone":
        print("Choose right option to start the fight (alone/with lucas)")
        quit()
    else:
        print("Choose the right option!")
        quit()

    print("First day is over alredy. Let's stop for a night")
    print("Game data saved")
    print(" ")

    
    #Second day

    print("It's morning alredy wake up")
    print(player_name + ": I had a weird a nightmare i still feel like someone is waching us")
    print("Lukas: I feel the same")

    print("Lukas: Okey enough talking time to head to the nearby town")
    print(player_name + ": How far is it")
    print("Lukas: We will get there in about 3 hour by walking speed")
    #Visiting Ragnorph's town
    print(player_name + ": Finally we are here")
    
    print("Lucas: I have to leave you alone for a while i have to meet someone here. You can explore town before i come back")
    mysterius_merchant = input("merchant: Hey you seem new here want to get some drinks?:(Yes/No) ")
    if mysterius_merchant.lower() == "yes":
        print(" ")
        print("In the town's bar")
        print(" ")
        print("merchant: I saw your fight with monster just outside the country")
        print(player_name + ":...")
        print("merchant: It was amazing. I have not seen someone as strong as you for a decade maybe.")
        print("merchant: I have a task for you there is a dragon in the nortwest from the town and it has been terorizing our country. Please help us defeat it")
        print(player_name + ": I will help you if you pay me 78 gold coins")
        print("merchant: Money is not a problem")
        print("You meet Lucas and he agreed to help you defeat the dragon")
        print("Lucas: leats just head to the hotel")
    elif mysterius_merchant.lower() == "no":
        print("merchant: Goodbay then!")
        print(player_name + ": Goodbay")
        print("You wait for several hours for lucas")
        print(player_name + ": You finnaly came, what took you so long")
        print("Lukas: I met a certain merchant and i have surprise for you")
        print(player_name + (": Tell me alredy"))
        print("Lukas: We are going to beat a dragon!")
        print(player_name + ": Whatt?")
        print("Lukas: It's long story leats just head to the hotel")
    else:
        print("Choose the right option!")
        quit()
    print("It's time to sleep since day is alredy over")
    print("Game data saved")
    
    #Third day

    print(" ")
    print("Lukas: Hey " + player_name + ": it's morning wake up time to kill the the dragon")
    print(player_name + ": Ughh alredy?")
    print("Lukas: What do you mean we are late alredy. Dragon lives very far from here we need to end before nightfall")
    
    print(player_name + ": Why does that even matters")
    print("Lukas: It's just a rumor but i heard that dragon gets stronger at night time")
    
    print("Lukas: Pack your things we are leaving")
    print(player_name + ": Okey okey")

    sleep_or_nah = input("Lukas went to get food for the journy. Want to sleep in the meantime?:(Yes/No)")
    if sleep_or_nah.lower() == "yes":
        print("Lukas: Hey what the heil are you doing i told you alredy that we are late get up fast")
        print(player_name + ": Okey i understandd ugh")
        points += 4
    elif sleep_or_nah.lower() == "no":
        print("Lukas: Oh you alredy packed your things. Thats great, lets go now shall we")
        print(" ")
        print("Evening came")
        print(" ")
    else:
        print("Choose the right option!")
        quit()

    #Into Before First Boss Fight
    print("Lukas: We are going to set our camp here and wait for the dragon")
    print(player_name + ": Hey i tought we should kill it before night comes")
    print("Lucas: I know that but we dont know were dragon currently is for safety it will be better to stay here and wait")
    print("I know we are taking a bit of a gamble but it's neccesary")    
    print(" ")
    print("Night Falls")
    print(" ")
    print("Lukas: It's about time dragon comes wait here and dont make a noise. I will go check surrounding areal")
    print("You hear a scream. Wait it's Lukas voice")
    print("You check and Lukas is on the ground now it's you against dragon")

    run_or_fight = input("Run Or Fight?(r/fight)")

    #Dark path
    if run_or_fight.lower() == "r":
        points -= 1
        print("You got away but lukas is not lucky enough")
        print(" ")
        print("Decade passed")
        print(" ")
        print("You feel bad for leaving lukas alone and now want to revange him")
        print("In the search of a dragon you became a hitman. On one unsuspecting normal day you accidentaly found")
        print(" ")
        print("The Dragon")
        print(" ")
        print("Game Begins")

        points += 10
        sneaky_attack = input("Dragon is sleeping attack him before he wakes up:(c/j) ")

        if sneaky_attack == "c":
            print("dragon took the hit bit barely took any damage")
        elif sneaky_attack == "j":
            print("dragon woke up and is now angry even tho your jab hit hard")
        print("It seems like the difference between you and dragon is too much")
        input("How do you plan defeating it:")
        print("That might work")
        block_or_dodge = input("dragon is charging a fireball attack try to neglect the damage: (d/b)")
        if block_or_dodge.lower() == "d":
            print("You dodged it")
        elif block_or_dodge.lower() == "b":
            print("You got burned alive")
        print("now it is your time to attack")
        input("type the attack:")
        print("Your attacks start to couse some damage. You are getting better at this")
        killer_move = input("dragon is using azura breath it usually is the killer move dodge it!!:")
        if killer_move.lower() == "d":
            print("You tried to dodge it but the attack still grazed you are 10% health")
        else:
            print("You died and respawned with 10% health")

        print("New skill activated: When you have have hp lower or equal to 10% you can use:")
        print(" ")
        print("' ATOMIC BREATH' ")
        print(" ")
        print("It is a same power as dragons azura breath. You awakened your copy ability")       
        final_blow = input("Use your new learned ability to finsh the dragon: ")
        if final_blow.lower() == "atomic breath":
            print("dragon is finished")
            print("you unlocked new title 'Dragon Killer' ")
        else:
            print("please use your new learned ability")
            quit()


    elif run_or_fight.lower() == "fight":
        points += 20
        sudden_attack = input("Dragon does not see you use any attack you desire: ")

        if sudden_attack == "c":
            print("dragon managed to dodge the counter punch even though you aimed from the blind spot")
        elif sudden_attack == "j":
            print("dragon counters your jab with a fireball")
            print("You unlocked new achievment 'Ouch thats hot'")
        print("It seems like the difference between you and dragon is too much")
        input("How do you plan defeating it:")
        print("That might work")
        block_or_dodge = input("dragon is charging a fireball attack try to neglect the damage: (d/b)")
        if block_or_dodge.lower() == "d":
            print("You dodged it")
        elif block_or_dodge.lower() == "b":
            print("You got burned alive")
        print("now it is your time to attack")
        input("type the attack:")
        print("Your attacks start to couse some damage. You are getting better at this")
        killer_move = input("dragon is using azura breath it usually is the killer move dodge it!!:")
        if killer_move.lower() == "d":
            print("You tried to dodge it but the attack still grazed you are 10% health")
        else:
            print("You died and respawned with 10% health")

        print("New skill activated: When you have have hp lower or equal to 10% you can use:")
        print(" ")
        print('"ATOMIC BREATH" ')
        print(" ")
        print("It is a same power as dragons azura breath. You awakened your copy ability.(press a to use atomic breath)")       
        final_blow = input("Use your new learned ability to finsh the dragon: ")
        if final_blow.lower() == "a":
            print("dragon is finished")
            print("you unlocked new title 'Dragon Killer' ")
            if " (The Honored One)" in player_name:
                player_name = player_name.replace(" (The Honored One)", " (Dragon Killer)")
            else:
                player_name += " (Dragon Killer)"
        else:
            print("please use your new learned ability")
            quit()
    else:
        print("Choose the right option!")
        quit()
    print(player_name+(": That was something unimaginable right?"))
    print("Lukas: I can't disagree about that")
    print(" ")
    print("Your points: "+ str(points))
    print(" ")
    
    print("Game Over")

#novice experience
if player_experience.lower() == "novice":
    print("You embarked on a serene camping trip with your family, deep in a dense forest. Amidst the beauty, you stumbled upon enigmatic symbols and strange whispers, eventually losing your way back to the campsite as darkness descended. Alone, you must navigate the unfamiliar woods, solve mysteries, and overcome dangers to reunite with your loved ones. Can you trust your instincts to guide you home?")
    #EXPERIENCE BEGINS!
    strange_voice = (input("Uhh! Whats that voice? Want to check the origins of this voice?: (yes/no)"))
    #If players checks the voice game agains otherwise it ends
    if strange_voice.lower() == "yes":
        print("Did you hear that? Over there look there is someone over there!")
        print("From the shadows emerges guy named lukas. His glowing red eyes lock onto yours. Lukas: You finally came traveller from today onwards you will experience the secrets of this world and you my friend are going to save everyone!")
    elif strange_voice.lower() == "no":
        print("You hide in the bushes till the morning and find your family. You leave forest unharmed with your family")
        quit()
    else:
        print("Choose the right option!")
        quit()

    #New character lukas
    input("Lukas: lets go alredy what are you waiting for: ")
    print(player_name+": Yeah but were are we going?")
    print("Lukas: Well i dunno you choose")

    location = input("Choose the location: ")

    print("Lukas: Okey so were heading to", location)

    first_fight = input("On the way to the " + location + " you encounter a monster. Do you want to fight it alone or get help from Lucas. (alone/with Lukas): ")
    
    experienced_bonuses = ["c = counter attack", "b = block", "d = dodge", "j = jab", "r = run"]
    print("basic attacks:")
    format_with_bullet_point(experienced_bonuses)

    print(" ")
    #First fight + way to gain points 
    if first_fight == "alone":
        points += 12
        move = input("monster is attacking from the left what do you do: (use c/b/d/j) ")
        if move == "d":
            print("Nice you dodged it")
        elif move == "c":
            print("Wow you sure got guts to counter mosnter but monster saw that coming and countered your counter")
        elif move == "b":
            print("You blocked but monster is really strong and it did some damage")
        elif move == "j":
            print("You were too slow monster hit you first")
        input("You have another opportunity to attack, use any attack you want?: ")
        print("I am amazed it only grazed the monster but yet monster got knocked down")
        honor_or_win = input("Attack the monster before it gets up. Do you attack?: (Yes/No)")
        if honor_or_win.lower() == "yes":
            print("Monster has been deleted from existence from your attack. Great Job")
        elif honor_or_win.lower() == "no":
            print("You now have earned a title 'The Honored One'")
            player_name += ' (The Honored One)'
            input("You are out of breath you need to finish this quickly use one final attack before monster attacks back. What do you do: ")
            print("Lukas: Good job that finished it")
        else:
            print("Choose the right option!")
            quit()
        
    elif first_fight.lower() == "with lucas":
        print("You dash and attack the monster a few times but it doesnt seem to harm him")
        print("Lukas: Move out for a moment it's my turn now")
        print("Lukas is on another level he beat monster with single blow")
        points += 7

    elif first_fight.lower() != "with lucas" or "alone":
        print("Choose right option to start the fight (alone/with lucas)")
        quit()

    print("First day is over alredy. Let's stop for a night")
    print("Game data saved")
    print(" ")

    
    #Second day

    print("It's morning alredy wake up")
    print(player_name + ": I had a weird a nightmare i still feel like someone is waching us")
    print("Lukas: I feel the same")

    print("Lukas: Okey enough talking time to head to the nearby town")
    print(player_name + ": How far is it")
    print("Lukas: We will get there in about 3 hour by walking speed")
    #Visiting Ragnorph's town
    print(player_name + ": Finally we are here")
    
    print("Lucas: I have to leave you alone for a while i have to meet someone here. You can explore town before i come back")
    mysterius_merchant = input("merchant: Hey you seem new here want to get some drinks?:(Yes/No) ")
    if mysterius_merchant.lower() == "yes":
        print(" ")
        print("In the town's bar")
        print(" ")
        print("merchant: I saw your fight with monster just outside the country")
        print(player_name + ":...")
        print("merchant: It was amazing. I have not seen someone as strong as you for a decade maybe.")
        print("merchant: I have a task for you there is a dragon in the nortwest from the town and it has been terorizing our country. Please help us defeat it")
        print(player_name + ": I will help you if you pay me 54 gold coins")
        print("merchant: Money is not a problem")
        print("You meet Lucas and he agreed to help you defeat the dragon")
        print("Lucas: leats just head to the hotel")
    elif mysterius_merchant.lower() == "no":
        print("merchant: Goodbay then!")
        print(player_name + ": Goodbay")
        print("You wait for several hours for lucas")
        print(player_name + ": You finnaly came, what took you so long")
        print("Lukas: I met a certain merchant and i have surprise for you")
        print(player_name + (": Tell me alredy"))
        print("Lukas: We are going to beat a dragon!")
        print(player_name + ": Whatt?")
        print("Lukas: It's long story leats just head to the hotel")
    else:
        print("Choose the right option!")
        quit()
    print("It's time to sleep since day is alredy over")
    print("Game data saved")
    
    #Third day

    print(" ")
    print("Lukas: Hey " + player_name + ": it's morning wake up time to kill the the dragon")
    print(player_name + ": Ughh alredy?")
    print("Lukas: What do you mean we are late alredy. Dragon lives very far from here we need to end before nightfall")
    
    print(player_name + ": Why does that even matters")
    print("Lukas: It's just a rumor but i heard that dragon gets stronger at night time")
    
    print("Lukas: Pack your things we are leaving")
    print(player_name + ": Okey okey")

    sleep_or_nah = input("Lukas went to get food for the journy. Want to sleep in the meantime?:(Yes/No)")
    if sleep_or_nah.lower() == "yes":
        print("Lukas: Hey what the heil are you doing i told you alredy that we are late get up fast")
        print(player_name + ": Okey i understandd ugh")
        points += 4
    elif sleep_or_nah.lower() == "no":
        print("Lukas: Oh you alredy packed your things. Thats great, lets go now shall we")
        print(" ")
        print("Evening came")
        print(" ")
    else:
        print("Choose the right option!")
        quit()

    #Into Before First Boss Fight
    print("Lukas: We are going to set our camp here and wait for the dragon")
    print(player_name + ": Hey i tought we should kill it before night comes")
    print("Lucas: I know that but we dont know were dragon currently is for safety it will be better to stay here and wait")
    print("I know we are taking a bit of a gamble but it's neccesary")    
    print(" ")
    print("Night Falls")
    print(" ")
    print("Lukas: It's about time dragon comes wait here and dont make a noise. I will go check surrounding areal")
    print("You hear a scream. Wait it's Lukas voice")
    print("You check and Lukas is on the ground now it's you against dragon")

    run_or_fight = input("Run Or Fight?(r/fight)")

    #Dark path
    if run_or_fight.lower() == "r":
        points -= 3
        print("You got away but lukas is not lucky enough")
        print(" ")
        print("Decade passed")
        print(" ")
        print("You feel bad for leaving lukas alone and now want to revange him")
        print("In the search of a dragon you became a hitman. On one unsuspecting normal day you accidentaly found")
        print(" ")
        print("The Dragon")
        print(" ")
        print("Game Begins")

        points += 10
        sneaky_attack = input("Dragon doesnt seem to see you attack him:(c/j) ")

        if sneaky_attack == "c":
            print("Dragon saw you and dodged your attack")
        elif sneaky_attack == "j":
            print("dragon saw that jab coming and blocked it")
        print("It seems like the difference between you and dragon is too much")
        print("It will be hard to defeat the dragon since you coundnt even hit him once")
        input("How do you plan defeating it:")
        print("That might work")
        block_or_dodge = input("dragon is charging a fireball attack try to neglect the damage: (d/b)")
        if block_or_dodge.lower() == "d":
            print("You dodged it")
        elif block_or_dodge.lower() == "b":
            print("You got burned alive")
            quit()
            
        print("now it is your time to attack")
        input("type the attack:")
        print("Your attacks start to couse some damage. You are getting better at this")
        killer_move = input("dragon is using azura breath it usually is the killer move dodge it!!:")
        if killer_move.lower() == "d":
            print("You tried to dodge it but the attack still grazed you are 7% health")
        elif killer_move.lower() == "b":
            print("You blocked but you are left with with 4% health")
        else:
            print("You died")
            quit()

        print("New skill activated: When you have have hp lower or equal to 7% you can use:")
        print(" ")
        print("' ATOMIC BREATH' ")
        print(" ")
        print("It is a same power as dragons azura breath. You awakened your copy ability")       
        final_blow = input("Use your new learned ability to finsh the dragon: ")
        if final_blow.lower() == "atomic breath":
            print("dragon is finished")
            print("you unlocked new title 'Dragon Killer' ")
        else:
            print("please use your new learned ability")
            quit()


    elif run_or_fight.lower() == "fight":
        points += 20
        sudden_attack = input("Dragon sees you be carefull with your attacks:(c/j) ")

        if sudden_attack == "c":
            print("dragon managed to dodge the counter punch even though you aimed from the blind spot")
        elif sudden_attack == "j":
            print("dragon counters your jab with a fireball")
            print("You unlocked new achievment 'Ouch thats hot'")
        input("Dragon is attacking defend yourself: ")
        print("Too bad it was too fast you coudnt do anything")
        print("Your HP = 48%")
        input("How do you plan defeating it:")
        print("That might work")
        block_or_dodge = input("dragon is charging a fireball attack try to neglect the damage: (d/b)")
        if block_or_dodge.lower() == "d":
            print("You dodged it")
        elif block_or_dodge.lower() == "b":
            print("You got burned alive")
            quit()

        print("now it is your time to attack")
        input("type the attack:")
        print("Your attacks start to couse some damage. You are getting better at this")
        killer_move = input("dragon is using azura breath it usually is the killer move dodge it!!:")
        if killer_move.lower() == "d":
            print("You tried to dodge it but the attack still grazed you are 7% health")
        elif killer_move.lower() == "b":
            print("You blocked but you are left with with 4% health")
        else:
            print("you died")
            quit()

        print("New skill activated: When you have have hp lower or equal to 7% you can use:")
        print(" ")
        print("' ATOMIC BREATH' ")
        print(" ")
        print("It is a same power as dragons azura breath. You awakened your copy ability.(press a to use atomic breath)")       
        final_blow = input("Use your new learned ability to finsh the dragon: ")
        if final_blow.lower() == "a":
            print("dragon is finished")
            print("you unlocked new title 'Dragon Killer' ")
            if " (The Honored One)" in player_name:
                player_name = player_name.replace(" (The Honored One)", " (Dragon Killer)")
            else:
                player_name += " (Dragon Killer)"
        else:
            print("please use your new learned ability")
            quit()
    else:
        print("Choose the right option!")
        quit()

    print(player_name+(": That was something unimaginable right?"))
    print("Lukas: I can't disagree about that")
    print(" ")
    print("Your points: "+ str(points))
    print(" ")
    
    print("Game Over")

if player_experience.lower() == "novice":
    print("You embarked on a serene camping trip with your family, deep in a dense forest. Amidst the beauty, you stumbled upon enigmatic symbols and strange whispers, eventually losing your way back to the campsite as darkness descended. Alone, you must navigate the unfamiliar woods, solve mysteries, and overcome dangers to reunite with your loved ones. Can you trust your instincts to guide you home?")
    #EXPERIENCE BEGINS!
    strange_voice = (input("Uhh! Whats that voice? Want to check the origins of this voice?: (yes/no)"))
    #If players checks the voice game agains otherwise it ends
    if strange_voice.lower() == "yes":
        print("Did you hear that? Over there look there is someone over there!")
        print("From the shadows emerges guy named lukas. His glowing red eyes lock onto yours. Lukas: You finally came traveller from today onwards you will experience the secrets of this world and you my friend are going to save everyone!")
    elif strange_voice.lower() == "no":
        print("You hide in the bushes till the morning and find your family. You leave forest unharmed with your family")
        quit()
    else:
        print("Choose the right option!")
        quit()

    #New character lukas
    input("Lukas: lets go alredy what are you waiting for: ")
    print(player_name+": Yeah but were are we going?")
    print("Lukas: Well i dunno you choose")

    location = input("Choose the location: ")

    print("Lukas: Okey so were heading to", location)

    first_fight = input("On the way to the " + location + " you encounter a monster. Do you want to fight it alone or get help from Lucas. (alone/with Lukas): ")
    
    experienced_bonuses = ["c = counter attack", "b = block", "d = dodge", "j = jab", "r = run"]
    print("basic attacks:")
    format_with_bullet_point(experienced_bonuses)

    print(" ")
    #First fight + way to gain points 
    if first_fight == "alone":
        points += 9
        move = input("monster is attacking from the left what do you do: (use c/b/d/j) ")
        if move == "d":
            print("Nice you dodged it")
        elif move == "c":
            print("Wow you sure got guts to counter mosnter but monster saw that coming and countered your counter")
        elif move == "b":
            print("You blocked but monster is really strong and it did some damage")
        elif move == "j":
            print("You were too slow monster hit you first")

        input("You have another opportunity to attack, use any attack you want?: ")
        print("I am amazed it only grazed the monster but yet monster got knocked down")
        honor_or_win = input("Attack the monster before it gets up. Do you attack?: (Yes/No)")

        if honor_or_win.lower() == "yes":
            print("Monster has been deleted from existence from your attack. Great Job")
        elif honor_or_win.lower() == "no":
            print("You now have earned a title 'The Honored One'")
            player_name += ' (The Honored One)'
            input("You are out of breath you need to finish this quickly use one final attack before monster attacks back. Which attack do you use: ")
            print("Monster got knocked down but he got up and continued fighting")
            print("He dissapeared? Look behind you!")
            print("He hit you with an uppercut")
            input("You look realy exhausted use finnal move to finish him: ")
            print("Lukas: Good job that definitely finished it")
        else:
            print("Choose the right option!")
            quit()
        
    elif first_fight.lower() == "with lucas":
        print("You dash and attack the monster a few times but it doesnt seem to harm him")
        print("Lukas: Move out for a moment it's my turn now")
        print("Lukas is on another level he beat monster with single blow")
        points += 4

    elif first_fight.lower() != "with lucas" or "alone":
        print("Choose right option to start the fight (alone/with lucas)")
        quit()

    print("First day is over alredy. Let's stop for a night")
    print("Game data saved")
    print(" ")

    
    #Second day

    print("It's morning alredy wake up")
    print(player_name + ": I had a weird a nightmare i still feel like someone is waching us")
    print("Lukas: I feel the same")

    print("Lukas: Okey enough talking time to head to the nearby town")
    print(player_name + ": How far is it")
    print("Lukas: We will get there in about 3 hour by walking speed")
    #Visiting Ragnorph's town
    print(player_name + ": Finally we are here")
    
    print("Lucas: I have to leave you alone for a while i have to meet someone here. You can explore town before i come back")
    mysterius_merchant = input("merchant: Hey you seem new here want to get some drinks?:(Yes/No) ")
    if mysterius_merchant.lower() == "yes":
        print(" ")
        print("In the town's bar")
        print(" ")
        print("merchant: I saw your fight with monster just outside the country")
        print(player_name + ":...")
        print("merchant: It was amazing. I have not seen someone as strong as you for a decade maybe.")
        print("merchant: I have a task for you there is a dragon in the nortwest from the town and it has been terorizing our country. Please help us defeat it")
        print(player_name + ": I will help you if you pay me 54 gold coins")
        print("merchant: Money is not a problem")
        print("You meet Lucas and he agreed to help you defeat the dragon")
        print("Lucas: leats just head to the hotel")
    elif mysterius_merchant.lower() == "no":
        print("merchant: Goodbay then!")
        print(player_name + ": Goodbay")
        print("You wait for several hours for lucas")
        print(player_name + ": You finnaly came, what took you so long")
        print("Lukas: I met a certain merchant and i have surprise for you")
        print(player_name + (": Tell me alredy"))
        print("Lukas: We are going to beat a dragon!")
        print(player_name + ": Whatt?")
        print("Lukas: It's long story leats just head to the hotel")
    else:
        print("Choose the right option!")
        quit()
    print("It's time to sleep since day is alredy over")
    print("Game data saved")
    
    #Third day

    print(" ")
    print("Lukas: Hey " + player_name + ": it's morning wake up time to kill the the dragon")
    print(player_name + ": Ughh alredy?")
    print("Lukas: What do you mean we are late alredy. Dragon lives very far from here we need to end before nightfall")
    
    print(player_name + ": Why does that even matters")
    print("Lukas: It's just a rumor but i heard that dragon gets stronger at night time")
    
    print("Lukas: Pack your things we are leaving")
    print(player_name + ": Okey okey")

    sleep_or_nah = input("Lukas went to get food for the journy. Want to sleep in the meantime?:(Yes/No)")
    if sleep_or_nah.lower() == "yes":
        print("Lukas: Hey what the heil are you doing i told you alredy that we are late get up fast")
        print(player_name + ": Okey i understandd ugh")
        points += 4
    elif sleep_or_nah.lower() == "no":
        print("Lukas: Oh you alredy packed your things. Thats great, lets go now shall we")
        print(" ")
        print("Evening came")
        print(" ")
    else:
        print("Choose the right option!")
        quit()

    #Into Before First Boss Fight
    print("Lukas: We are going to set our camp here and wait for the dragon")
    print(player_name + ": Hey i tought we should kill it before night comes")
    print("Lucas: I know that but we dont know were dragon currently is for safety it will be better to stay here and wait")
    print("I know we are taking a bit of a gamble but it's neccesary")    
    print(" ")
    print("Night Falls")
    print(" ")
    print("Lukas: It's about time dragon comes wait here and dont make a noise. I will go check surrounding areal")
    print("You hear a scream. Wait it's Lukas voice")
    print("You check and Lukas is on the ground now it's you against dragon")

    run_or_fight = input("Run Or Fight?(r/fight)")

    #Dark path
    if run_or_fight.lower() == "r":
        points -= 3
        print("You got away but lukas is not lucky enough")
        print(" ")
        print("Decade passed")
        print(" ")
        print("You feel bad for leaving lukas alone and now want to revange him")
        print("In the search of a dragon you became a hitman. On one unsuspecting normal day you accidentaly found")
        print(" ")
        print("The Dragon")
        print(" ")
        print("Game Begins")

        points += 8
        sneaky_attack = input("Dragon doesnt seem to see you attack him:(c/j) ")

        if sneaky_attack == "c":
            print("Dragon saw you and dodged your attack")
        elif sneaky_attack == "j":
            print("dragon saw that jab coming and blocked it")
        print("It seems like the difference between you and dragon is too much")
        print("It will be hard to defeat the dragon since you coundnt even hit him once")
        input("How do you plan defeating it:")
        print("That might work")
        block_or_dodge = input("dragon is charging a fireball attack try to neglect the damage: (d/b)")
        if block_or_dodge.lower() == "d":
            print("You dodged it")
        elif block_or_dodge.lower() == "b":
            print("You got burned alive")
            quit()
            
        print("now it is your time to attack")
        input("type the attack:")
        print("Your attacks start to couse some damage. You are getting better at this")
        killer_move = input("dragon is using azura breath it usually is the killer move dodge it!!:")
        if killer_move.lower() == "d":
            print("You tried to dodge it but the attack still grazed you are 6% health")
        elif killer_move.lower() == "b":
            print("You blocked but you are left with with 3% health")
        else:
            print("You died")
            quit()

        print("New skill activated: When you have have hp lower or equal to 6% you can use:")
        print(" ")
        print("' ATOMIC BREATH' ")
        print(" ")
        print("It is a same power as dragons azura breath. You awakened your copy ability")       
        final_blow = input("Use your new learned ability to finsh the dragon: ")
        if final_blow.lower() == "atomic breath":
            print("dragon is finished")
            print("you unlocked new title 'Dragon Killer' ")
        else:
            print("please use your new learned ability")
            quit()


    elif run_or_fight.lower() == "fight":
        points += 16
        sudden_attack = input("Dragon sees you be carefull with your attacks:(c/j) ")

        if sudden_attack == "c":
            print("dragon managed to dodge the counter punch even though you aimed from the blind spot")
        elif sudden_attack == "j":
            print("dragon counters your jab with a fireball")
            print("You unlocked new achievment 'Ouch thats hot'")
        input("Dragon is attacking defend yourself: ")
        print("Too bad it was too fast you coudnt do anything")
        print("Your HP = 48%")
        input("How do you plan defeating it: ")
        print("That might work")
        block_or_dodge = input("dragon is charging a fireball attack try to neglect the damage: (d/b)")
        if block_or_dodge.lower() == "d":
            print("You dodged it")
        elif block_or_dodge.lower() == "b":
            print("You got burned alive")
            quit()

        print("now it is your time to attack")
        input("type the attack:")
        print("Your attacks start to couse some damage. You are getting better at this")
        killer_move = input("dragon is using azura breath it usually is the killer move dodge it!!:")
        if killer_move.lower() == "d":
            print("You tried to dodge it but the attack still grazed you are 6% health")
        elif killer_move.lower() == "b":
            print("You blocked but you are left with with 3% health")
        else:
            print("you died")
            quit()

        print("New skill activated, When you have have hp lower or equal to 6% you can use:")
        print(" ")
        print("' ATOMIC BREATH' ")
        print(" ")
        print("It is a same power as dragons azura breath. You awakened your copy ability.(press 'a' to use atomic breath)")       
        final_blow = input("Use your new learned ability to finsh the dragon: ")
        if final_blow.lower() == "a":
            print("dragon is finished")
            print("you unlocked new title 'Dragon Killer' ")
            if " (The Honored One)" in player_name:
                player_name = player_name.replace(" (The Honored One)", " (Dragon Killer)")
            else:
                player_name += " (Dragon Killer)"
        else:
            print("please use your new learned ability")
            quit()
    else:
        print("Choose the right option!")
        quit()
        
    print(player_name+(": That was something unimaginable right?"))
    print("Lukas: I can't disagree about that")
    print(" ")
    print("Your points: "+ str(points))
    print(" ")
    
    print("Game Over")

#expert player's experience
if player_experience.lower() == "expert":
    print("You embarked on a serene camping trip with your family, deep in a dense forest. Amidst the beauty, you stumbled upon enigmatic symbols and strange whispers, eventually losing your way back to the campsite as darkness descended. Alone, you must navigate the unfamiliar woods, solve mysteries, and overcome dangers to reunite with your loved ones. Can you trust your instincts to guide you home?")
    #EXPERIENCE BEGINS!
    strange_voice = (input("Uhh! Whats that voice? Want to check the origins of this voice?: (yes/no)"))
    #If players checks the voice game agains otherwise it ends
    if strange_voice.lower() == "yes":
        print("Did you hear that? Over there look there is someone over there!")
        print("From the shadows emerges guy named lukas. His glowing red eyes lock onto yours. Lukas: You finally came traveller from today onwards you will experience the secrets of this world and you my friend are going to save everyone!")
    elif strange_voice.lower() == "no":
        print("You hide in the bushes till the morning and find your family. You leave forest unharmed with your family")
        quit()
    else:
        print("Choose the right option!")
        quit()

    #New character lukas
    input("Lukas: lets go alredy what are you waiting for: ")
    print(player_name+": Yeah but were are we going?")
    print("Lukas: Well i dunno you choose")

    location = input("Choose the location: ")

    print("Lukas: Okey so were heading to", location)

    first_fight = input("On the way to the " + location + " you encounter a monster. Do you want to fight it alone or get help from Lucas. (alone/with Lukas): ")
    
    experienced_bonuses = ["c = counter attack", "b = block", "d = dodge", "j = jab", "r = run"]
    print("basic attacks:")
    format_with_bullet_point(experienced_bonuses)

    print(" ")
    #First fight + way to gain points 
    if first_fight == "alone":
        points += 9
        move = input("monster is attacking from the left what do you do: (use c/b/d/j) ")
        if move == "d":
            print("Nice you dodged it")
        elif move == "c":
            print("Wow you sure got guts to counter mosnter but monster saw that coming and countered your counter")
        elif move == "b":
            print("You blocked but monster is really strong and it did some damage")
        elif move == "j":
            print("You were too slow monster hit you first")

        input("You have another opportunity to attack, use any attack you want?: ")
        print("I am amazed it only grazed the monster but yet monster got knocked down")
        honor_or_win = input("Attack the monster before it gets up. Do you attack?: (Yes/No)")

        if honor_or_win.lower() == "yes":
            print("Monster has been deleted from existence from your attack. Great Job")
        elif honor_or_win.lower() == "no":
            print("You now have earned a title 'The Honored One'")
            player_name += ' (The Honored One)'
            input("You are out of breath you need to finish this quickly use one final attack before monster attacks back. Which attack do you use: ")
            print("Monster got knocked down but he got up and continued fighting")
            print("He dissapeared? Look behind you!")
            print("He hit you with an uppercut")
            input("You look realy exhausted use finnal move to finish him: ")
            print("Lukas: Good job that definitely finished it")
        else:
            print("Choose the right option!")
            quit()
        
    elif first_fight.lower() == "with lucas":
        print("You dash and attack the monster a few times but it doesnt seem to harm him")
        print("Lukas: Move out for a moment it's my turn now")
        print("Lukas is on another level he beat monster with single blow")
        points += 4

    elif first_fight.lower() != "with lucas" or "alone":
        print("Choose right option to start the fight (alone/with lucas)")
        quit()

    print("First day is over alredy. Let's stop for a night")
    print("Game data saved")
    print(" ")

    
    #Second day

    print("It's morning alredy wake up")
    print(player_name + ": I had a weird a nightmare i still feel like someone is waching us")
    print("Lukas: I feel the same")

    print("Lukas: Okey enough talking time to head to the nearby town")
    print(player_name + ": How far is it")
    print("Lukas: We will get there in about 3 hour by walking speed")
    #Visiting Ragnorph's town
    print(player_name + ": Finally we are here")
    
    print("Lucas: I have to leave you alone for a while i have to meet someone here. You can explore town before i come back")
    mysterius_merchant = input("merchant: Hey you seem new here want to get some drinks?:(Yes/No) ")
    if mysterius_merchant.lower() == "yes":
        print(" ")
        print("In the town's bar")
        print(" ")
        print("merchant: I saw your fight with monster just outside the country")
        print(player_name + ":...")
        print("merchant: It was amazing. I have not seen someone as strong as you for a decade maybe.")
        print("merchant: I have a task for you there is a dragon in the nortwest from the town and it has been terorizing our country. Please help us defeat it")
        print(player_name + ": I will help you if you pay me 54 gold coins")
        print("merchant: Money is not a problem")
        print("You meet Lucas and he agreed to help you defeat the dragon")
        print("Lucas: leats just head to the hotel")
    elif mysterius_merchant.lower() == "no":
        print("merchant: Goodbay then!")
        print(player_name + ": Goodbay")
        print("You wait for several hours for lucas")
        print(player_name + ": You finnaly came, what took you so long")
        print("Lukas: I met a certain merchant and i have surprise for you")
        print(player_name + (": Tell me alredy"))
        print("Lukas: We are going to beat a dragon!")
        print(player_name + ": Whatt?")
        print("Lukas: It's long story leats just head to the hotel")
    else:
        print("Choose the right option!")
        quit()
    print("It's time to sleep since day is alredy over")
    print("Game data saved")
    
    #Third day

    print(" ")
    print("Lukas: Hey " + player_name + ": it's morning wake up time to kill the the dragon")
    print(player_name + ": Ughh alredy?")
    print("Lukas: What do you mean we are late alredy. Dragon lives very far from here we need to end before nightfall")
    
    print(player_name + ": Why does that even matters")
    print("Lukas: It's just a rumor but i heard that dragon gets stronger at night time")
    
    print("Lukas: Pack your things we are leaving")
    print(player_name + ": Okey okey")

    sleep_or_nah = input("Lukas went to get food for the journy. Want to sleep in the meantime?:(Yes/No)")
    if sleep_or_nah.lower() == "yes":
        print("Lukas: Hey what the heil are you doing i told you alredy that we are late get up fast")
        print(player_name + ": Okey i understandd ugh")
        points += 2
    elif sleep_or_nah.lower() == "no":
        print("Lukas: Oh you alredy packed your things. Thats great, lets go now shall we")
        print(" ")
        print("Evening came")
        print(" ")
    else:
        print("Choose the right option!")
        quit()

    #Into Before First Boss Fight
    print("Lukas: We are going to set our camp here and wait for the dragon")
    print(player_name + ": Hey i tought we should kill it before night comes")
    print("Lucas: I know that but we dont know were dragon currently is for safety it will be better to stay here and wait")
    print("I know we are taking a bit of a gamble but it's neccesary")    
    print(" ")
    print("Night Falls")
    print(" ")
    print("Lukas: It's about time dragon comes wait here and dont make a noise. I will go check surrounding areal")
    print("You hear a scream. Wait it's Lukas voice")
    print("You check and Lukas is on the ground now it's you against dragon")

    run_or_fight = input("Run Or Fight?(r/fight)")

    #Dark path
    if run_or_fight.lower() == "r":
        points -= 6
        print("You got away but lukas is not lucky enough")
        print(" ")
        print("Decade passed")
        print(" ")
        print("You feel bad for leaving lukas alone and now want to revange him")
        print("In the search of a dragon you became a hitman. On one unsuspecting normal day you accidentaly found")
        print(" ")
        print("The Dragon")
        print(" ")
        print("Game Begins")

        points += 3
        sneaky_attack = input("Dragon doesnt seem to see you attack him:(c/j) ")

        if sneaky_attack == "c":
            print("Dragon saw you and dodged your attack")
        elif sneaky_attack == "j":
            print("dragon saw that jab coming and blocked it")
        print("It seems like the difference between you and dragon is too much")
        print("It will be hard to defeat the dragon since you coundnt even hit him once")
        input("How do you plan defeating it:")
        print("That might work")
        block_or_dodge = input("dragon is charging a fireball attack try to neglect the damage: (d/b)")
        if block_or_dodge.lower() == "d":
            print("You dodged it")
        elif block_or_dodge.lower() == "b":
            print("You got burned alive")
            quit()
            
        print("now it is your time to attack")
        input("type the attack:")
        print("Your attacks start to couse some damage. You are getting better at this")
        print("Ups you got unlucky 10 second blindness activated!")
        print("Dragon is taking advantage of it here comes the barrack of punches from monster")
        print("you are now in critical situation")
        print("It seems like dragon is trying to finish you off")
        killer_move = input("dragon is using azura breath it usually is the killer move dodge it!!:")
        if killer_move.lower() == "d":
            print("You tried to dodge it but the attack still grazed you are 3% health")
        elif killer_move.lower() == "b":
            print("You blocked but you are left with with 1% health")
        else:
            print("You died")
            quit()

        print("New skill activated: When you have have hp lower or equal to 6% you can use:")
        print(" ")
        print("' ATOMIC BREATH' ")
        print(" ")
        print("It is a same power as dragons azura breath. You awakened your copy ability")       
        final_blow = input("Use your new learned ability to finsh the dragon: ")
        if final_blow.lower() == "atomic breath":
            print("dragon is finished")
            print("you unlocked new title 'Dragon Killer' ")
        else:
            print("please use your new learned ability")
            quit()


    elif run_or_fight.lower() == "fight":
        points += 11
        sudden_attack = input("Dragon sees you be carefull with your attacks:(c/j) ")

        if sudden_attack == "c":
            print("dragon managed to dodge the counter punch even though you aimed from the blind spot")
        elif sudden_attack == "j":
            print("dragon counters your jab with a fireball")
            print("You unlocked new achievment 'Ouch thats hot'")
        input("Dragon is attacking defend yourself: ")
        print("Too bad it was too fast you coudnt do anything")
        print("Your HP = 48%")
        input("How do you plan defeating it: ")
        print("That might work")
        block_or_dodge = input("dragon is charging a fireball attack try to neglect the damage: (d/b)")
        if block_or_dodge.lower() == "d":
            print("You dodged it")
        elif block_or_dodge.lower() == "b":
            print("You got burned alive")
            quit()

        print("now it is your time to attack")
        input("type the attack:")
        print("Your attacks start to couse some damage. You are getting better at this")
        print("Ups you got unlucky 10 second blindness activated!")
        print("Dragon is taking advantage of it here comes the barrack of punches from monster")
        print("you are now in critical situation")
        print("It seems like dragon is trying to finish you off")
        killer_move = input("dragon is using azura breath it usually is the killer move dodge it!!:")
        if killer_move.lower() == "d":
            print("You tried to dodge it but the attack still grazed you are 3% health")
        elif killer_move.lower() == "b":
            print("You blocked but you are left with with 1% health")
        else:
            print("you died")
            quit()

        print("New skill activated, When you have have hp lower or equal to 3% you can use:")
        print(" ")
        print("' ATOMIC BREATH' ")
        print(" ")
        print("It is a same power as dragons azura breath. You awakened your copy ability.(press 'a' to use atomic breath)")       
        final_blow = input("Use your new learned ability to finsh the dragon: ")
        if final_blow.lower() == "a":
            print("dragon is finished")
            print("you unlocked new title 'Dragon Killer' ")
            if " (The Honored One)" in player_name:
                player_name = player_name.replace(" (The Honored One)", " (Dragon Killer)")
            else:
                player_name += " (Dragon Killer)"
        else:
            print("please use your new learned ability")
            quit()
    else:
        print("Choose the right option!")
        quit()
        
    print(player_name+(": That was something unimaginable right?"))
    print("Lukas: I can't disagree about that")
    print("You faint from exhaustion")
    print(" ")
    print("Your points: "+ str(points))
    print(" ")
    
    print("Game Over")