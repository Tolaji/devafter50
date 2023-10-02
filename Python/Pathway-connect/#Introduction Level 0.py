# Import 'random' module  to select items from list
import random

# define the function to play game

# Level 0 Introduction
print("\n ~~~~~~~~ Introduction ~~~~~~~\n")
print(
    "\nWelcome to this nail-biting adventure game! You are about to embark on a\ndangerous journey filled with tough decisions. You will encounter different \nscenarios and will have to make choices that will determine your fate.\nAre you ready?\n"
)
# Level 1
print("Imagine yourself hiking alone in the woods when you hear a loud growl.")
print("You turn around and see a huge bear staring at you")
print("What do you do?")
print()
make_decision = input("RUN\nPLAY_DEAD\nFIGHT\nEnter your choice: ")
print()

# Decision to run
if make_decision.upper() == "RUN":
    print("You start running as fast as you can.")
    print("You can hear the bear's footsteps behind you.")
    print("You come across a river, and you have to make a decision.")
    print()
    run = input("SWIM across river\nCROSS bridge\nEnter your choice: ")
    print()

    # Make a decision at the river to swim across
    if run.upper() == "SWIM":
        print("You jump into the river and start swimming")
        print("The current is strong, but you manage to reach the other side.")
        print("You look back and see the bear standing on the other side of the river.")
        print("You are safe for now")
        print()

    # Make a decision at the river to cross bridge
    if run.upper() == "CROSS":
        print("You run towards the bridge and start crossing it.")
        print("The bear catches up with you and starts attacking you.")
        print("You fight back, but the bear is too strong.")
        print("GAME OVER")
        print()

    else:
        print("Invalid input. GAME OVER.")
        print()

# Decision to fight
if make_decision.upper() == "FIGHT":
    print("You fought the bear, but it was too strong. ")
    print("GAME OVER")
    print()

# Decision to Play dead
if make_decision.upper() == "PLAY_DEAD":
    print("The bear approaches you and sniffs around.")
    print("You remain still, and the bear eventually loses interest and leaves.")
    print("You continue your hike")
    print()

    # Welcome to level 2

    print("You proceed to level 2")
    print("You come across an abandoned house in the middle of the woods.")
    print("You hear strange noises coming from inside the house.")
    print()

    # Decide what to do on approaching house
    house_decision = input("ENTER the house\nCONTINUE your hike\nEnter your choice: ")
    print()

    # Make decision to enter the house
    if house_decision.upper() == "ENTER":
        print("You enter the house and find yourself in a dark room.")
        print("You can't see anything, but you hear footsteps coming towards you.")
        print()
        house_activity = input("LIGHT_MATCH\nSTAY_STILL\nEnter your choice: ")
        print()

        # Decision to light a match; game over
        if house_activity.upper() == "LIGHT_MATCH":
            print(
                "You light a match, and you see a ghost standing right in front of you."
            )
            print("You scream and run out of the house.")
            print()
            print("GAME OVER")

        # Decision to stay still
        elif house_activity.upper() == "STAY_STILL":
            print("The footsteps stop, and the room becomes silent.")
            print(
                "You wait for a few minutes and then slowly make your way out of the house."
            )
            print("GAME OVER")
            print()

        else:
            print("Invalid input. Try again.")
            print()

    # Make decision to continue the hike
    elif house_decision.upper() == "CONTINUE":
        print("You keep walking and come across a river")
        print()
        river_decision = input("SWIM across\nCROSS the bridge\nEnter your choice: ")
        print()

        # River decision to swim
        if river_decision.upper() == "SWIM":
            print("You jump into the river and start swimming, the current is strong")
            print(
                "but you manage to reach the other side. You sustain injuries and exhausted"
            )
            print()
            print("GAME OVER")
            print()

        # River decision to cross
        elif river_decision.upper() == "CROSS":
            print("You cross the bridge and see a group of bandits waiting for you")
            print("They attack you, and you have to fight back")
            print("You manage to defeat them and continue your hike.")
            print()

            # Welcome to level 3
            print("You proceed to level 3")
            print("You come across a fork in the road.")
            print()

            # Decide what to do at T Junction on path to follow
            t_junction_decision = input(
                "Take the LEFT_PATH\nTake the RIGHT_PATH\nGO_BACK\nEnter your choice: "
            )
            print()

            # Take decision on after taking left path
            if t_junction_decision.upper() == "LEFT_PATH":
                print("You start walking down the left path and come across a cave.")
                print()
                cave_decision = input(
                    "OPEN the chest\n LEAVE the cave\nEnter your choice: "
                )
                print()

                # Open the chest
                if cave_decision.upper() == "OPEN":
                    print("The chest is booby-trapped, and you trigger a trap.")
                    print("GAME OVER")

                # Leave the cave
                elif cave_decision.upper() == "LEAVE":
                    print("You leave the cave and continue your hike.")
                    # Proceed on any key strike
                    print("Press any key to continue")
                    proceed_hike = ""

                    if proceed_hike == "":
                        print(
                            "You keep walking down the path and come across a group of wolves"
                        )
                        print()

                        # Decision to run away or fight wolves
                        on_hike_decision = input(
                            "RUN_AWAY\nFIGHT_BACK\nEnter your choice: "
                        )
                        print()

                        # Run away and game over
                        if on_hike_decision.upper() == "RUN_AWAY":
                            print(
                                "You start running, but the wolves catch up to you and attack you."
                            )
                            print("GAME OVER")
                            print()

                        # fight the wolves
                        elif on_hike_decision.upper() == "FIGHT_BACK":
                            print(
                                "You manage to defeat the wolves and continue your hike."
                            )
                            print(
                                "Congratulations, you have completed the nail-biting adventure game! Your choices have determined your fate, and you have made it through alive."
                            )
                            print()

                    else:
                        print("Invalid input. Try again.")
                        print()

            # Take decision on after taking right path
            elif t_junction_decision.upper() == "RIGHT_PATH":
                print("You start walking down the right path and come across a river.")
                print()

                # What to do at river
                river_crossing = input(
                    "SWIM across\nCROSS the bridge\nEnter your choice: "
                )

                # Chose to swim across
                if river_crossing.upper() == "SWIM":
                    print("You jump into the river and start swimming")
                    print(
                        "The current is strong, but you manage to reach the other side"
                    )
                    print("You continue your hike.")
                    print(
                        "Congratulations, you have completed the nail-biting adventure game! Your choices have determined your fate, and you have made it through alive."
                    )
                    print()

                # Chose to cross the bridge
                elif river_crossing.upper() == "CROSS":
                    print(
                        "You cross the bridge and see a group of bandits waiting for you"
                    )
                    print("They attack you, and you have to fight back")
                    print("You manage to defeat them and continue your hike.")
                    print(
                        "Congratulations, you have completed the nail-biting adventure game! Your choices have determined your fate, and you have made it through alive."
                    )
                    print()

            # Take decision to go back previous level
            elif t_junction_decision.upper() == "GO_BACK":
                print("You go back to no where in particular.")
                print("GAME OVER")
                print()

            else:
                print("Invalid input. Try again.")
                print()

        else:
            print("Invalid input. Try again.")
            print()

    else:
        print("Invalid input. Try again.")
        print()

else:
    print("Invalid input. Try again.")
    print()
