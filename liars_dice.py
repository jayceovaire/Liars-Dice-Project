# Liar's Dice
import math
import random
player_prompt = "How many players will be in this game?\n"
player_prompt += "(2-4 can play) type 'quit' to exit.\n:"


#def dice_roll()

#will roll 5 dice per player.
#total possible rolled is 20 dice
#dice dicionary will be assigned values based on outcomes of rolls -
#player will be shown what they rolled

#def player_turn()

#player will make a claim of how many dice of a specific value are on the board
#other players can choose to call liar and dice are revealed
#if player is lying they lose, if not, accusor loses.





player_1 = [1, 2, 3, 4, 5]
player_1_dice = []

player_2 = [1, 2, 3, 4, 5]
player_2_dice = []

player_3 = [1, 2, 3, 4, 5]
player_3_dice = []

player_4 = [1, 2, 3, 4, 5]
player_4_dice = []
total_dice = 0

class Player:
    def __init__(self, player_name, difficulty, playstyle):
        self.playername = player_name
        self.difficulty = difficulty
        self.playstyle = playstyle
    def describeplayer(self):
        print(f"{self.playername} has a difficulty of {self.difficulty}")
        print(f"Playstyle - {self.playstyle}\n")

bootstrap_bill = Player('Bootstrap Bill', 1, 'Honest')
crabman = Player('Crab-Man', 3, 'Less honest')
will_turner = Player('Will Turner', 5, 'Somewhat honest')
shark_head = Player('Shark Head', 7, 'liar')
jack_sparrow = Player('Captain Jack Sparrow', '"?"', 'random')
davey_jones = Player('Davey Jones', 10, 'The Devil')

def choose_player():
    print("Who will be in this game?"
    print(f"")
    #ADD MENU CHOICES OF PLAYERS POSSIBLE TO ADD TO GAME
    #List all possible choices
    #player can only add players up to number they chose but no more than 4
    # after choosing name must be taken off displayed choices


def main_menu():
    while True:

            players = (input(player_prompt))
            if players.lower() == 'quit':
                break
            elif players != 'quit':

                if players.isdigit():
                    if int(players) >= 2 and int(players) <= 4:
                        print(f"{players}, players eh? That'll do.\n ")
                        total_dice = int(players) * 5
                        print(f"So we be be playin' with {players} players and {total_dice} dice. ")
                        print(f" Who shall you be playing against?")
                        choose_player()
                        print("\n....Roll em' matey.\n")
                        roll = (input("Press Enter to roll your dice"))
                        break
                    else:
                        print("Between 2 and 4 players mate.\n ")


                        pass
main_menu()

def diceroll(playernumber,playerdice):
    for dice in playernumber:

        dice = (random.randint(1,6))
        playerdice.append(dice)

        print(dice)

diceroll(player_1,player_1_dice)
print(player_1_dice)

#roll dice for each player, random. range 1,6
# add numbers rolled to each players list











