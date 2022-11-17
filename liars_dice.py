# Liar's Dice
import math

player_prompt = "How many players will be in this game?\n"
player_prompt += "(2-4 can play) type 'quit' to exit.\n:"
total_dice = []

#def dice_roll()

#will roll 5 dice per player.
#total possible rolled is 20 dice
#dice dicionary will be assigned values based on outcomes of rolls -
#player will be shown what they rolled

#def player_turn()

#player will make a claim of how many dice of a specific value are on the board
#other players can choose to call liar and dice are revealed
#if player is lying they lose, if not, accusor loses.


def main_menu():
    while True:

            players = (input(player_prompt))
            if players.lower() == 'quit':
                break
            elif players != 'quit':

                if players.isdigit():
                    if int(players) >= 2 and int(players) <= 4:
                        print(f"{players}, players eh? That'll do.\n ")
                    else:
                        print("Between 2 and 4 players mate.\n ")


                        pass
main_menu()
print("we did it")

