# Liar's Dice
import math
import time
import random

player_prompt = "How many players will be in this game?\n"
player_prompt += "(2-4 can play) type 'quit' to exit.\n:"
chosen_players = []
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
opponent_list = ['Davey Jones', 'Captain Jack Sparrow', 'Shark Head', 'Will Turner', 'Crab-Man', 'Bootstrap Bill']
playing_opponents = []
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

def how_to_play():
    print("HOW TO PLAY README HERE")
    print(opponent_list)
# Write long explanation of how to play game

def main():
    title()
    main_menu()

def title():
    print("\n")
    print("$$\       $$\                   $$\               $$$$$$$\  $$\ ")
    print("$$ |      \__|                  $  |              $$  __$$\ \__|")
    print("$$ |      $$\  $$$$$$\   $$$$$$\\_/$$$$$$$\       $$ |  $$ |$$\  $$$$$$$\  $$$$$$\  ")
    print("$$ |      $$ | \____$$\ $$  __$$\ $$  _____|      $$ |  $$ |$$ |$$  _____|$$  __$$\ ")
    print("$$ |      $$ | $$$$$$$ |$$ |  \__|\$$$$$$\        $$ |  $$ |$$ |$$ /      $$$$$$$$ |")
    print("$$ |      $$ |$$  __$$ |$$ |       \____$$\       $$ |  $$ |$$ |$$ |      $$   ____|")
    print("$$$$$$$$\ $$ |\$$$$$$$ |$$ |      $$$$$$$  |      $$$$$$$  |$$ |\$$$$$$$\ \$$$$$$$\ ")
    print("\________|\__| \_______|\__|      \_______/       \_______/ \__| \_______| \_______|")
    print("____________________________________________________________________________________")

def main_menu():
    print("What would you like to do?\n--------------------------")
    print("1 : Play New Game\n2 : How to Play\n3 : Opponent Info\n4 : Quit")
    while True:
        main_menu_prompt = input(': ')

        if main_menu_prompt == "1":
                break

        elif main_menu_prompt == "2":
                how_to_play()
        elif main_menu_prompt == "3":
                bootstrap_bill.describeplayer()
                crabman.describeplayer()
                will_turner.describeplayer()
                shark_head.describeplayer()
                jack_sparrow.describeplayer()
                davey_jones.describeplayer()
        elif main_menu_prompt == "4":
            exit()
        else:
            main_menu()
    intro()

def intro():
            players = (input(player_prompt))
            if players.lower() == 'quit':
                exit()
            elif players != 'quit':

                if players.isdigit():
                    if int(players) >= 2 and int(players) <= 4:
                        number_players = players
                        number_of_players = players
                        print(f"{players}, players eh? That'll do.\n ")
                        input('(press enter to continue)\n')
                        total_dice = int(players) * 5
                        print(f"So we be be playin' with {players} players and {total_dice} dice.\n ")
                        input('(press enter to continue)\n')
                        choose_player(number_players)

                else:
                    print("Between 2 and 4 players mate.\n ")


def choose_player(number_players):
    print(f"Who shall you be playing against?")

    if number_players == '2':
        MAX_PLAYERS = 1
        for MAX_PLAYERS in range(1, MAX_PLAYERS + 1):
            for index, opponent in enumerate(opponent_list, 1):
                print(index, ': ' + opponent)


        if number_players == '2':
            chosen_player = input("Enter a number to choose an opponent:")
            if chosen_player == '1':
                print("You chose Davey Jones")
                opponent_list.remove("Davey Jones")
                playing_opponents.append('Davey Jones')

            elif chosen_player == '2':
                print("You chose Captain Jack Sparrow")
                opponent_list.remove("Captain Jack Sparrow")
                playing_opponents.append('Captain Jack Sparrow')

            elif chosen_player == '3':
                print("You chose Shark Head")
                opponent_list.remove("Shark Head")
                playing_opponents.append('Shark Head')

            elif chosen_player == '4':
                print("You chose Will Turner")
                opponent_list.remove("Will Turner")
                playing_opponents.append('Will Turner')

            elif chosen_player == '5':
                print("You chose Crab-Man")
                opponent_list.remove("Crab-Man")
                playing_opponents.append("Crab-Man")

            elif chosen_player == '6':
                print("You chose Bootstrap Bill")
                opponent_list.remove('Bootstrap Bill')
                playing_opponents.append('Bootstrap Bill')
            else:
                choose_player('2')





    elif number_players == '3':
        MAX_PLAYERS = 2
        for MAX_PLAYERS in range(1, MAX_PLAYERS + 1):

            for i, opponent in enumerate(opponent_list, 1):
                print(i, ': ' + opponent)
            if number_players == '3':
                chosen_player = input("Enter a number to choose an opponent:")
                if chosen_player == '1':
                    print("You chose Davey Jones")
                    opponent_list.remove("Davey Jones")
                    playing_opponents.append('Davey Jones')

                elif chosen_player == '2':
                    print("You chose Captain Jack Sparrow")
                    opponent_list.remove("Captain Jack Sparrow")
                    playing_opponents.append('Captain Jack Sparrow')

                elif chosen_player == '3':
                    print("You chose Shark Head")
                    opponent_list.remove("Shark Head")
                    playing_opponents.append('Shark Head')

                elif chosen_player == '4':
                    print("You chose Will Turner")
                    opponent_list.remove("Will Turner")
                    playing_opponents.append('Will Turner')

                elif chosen_player == '5':
                    print("You chose Crab-Man")
                    opponent_list.remove("Crab-Man")
                    playing_opponents.append("Crab-Man")

                elif chosen_player == '6':
                    print("You chose Bootstrap Bill")
                    opponent_list.remove('Bootstrap Bill')
                    playing_opponents.append('Bootstrap Bill')

                else:
                    choose_player('3')

    elif number_players == '4':
        MAX_PLAYERS = 3
        for MAX_PLAYERS in range(1,MAX_PLAYERS + 1):

            for i, opponent in enumerate(opponent_list, 1):
                print(i, ': ' + opponent)
            if number_players =='4':
                chosen_player = input("Enter a number to choose an opponent:")
                if chosen_player == '1':
                    print("You chose Davey Jones")
                    opponent_list.remove("Davey Jones")
                    playing_opponents.append('Davey Jones')


                elif chosen_player == '2':
                    print("You chose Captain Jack Sparrow")
                    opponent_list.remove("Captain Jack Sparrow")
                    playing_opponents.append('Captain Jack Sparrow')


                elif chosen_player == '3':
                    print("You chose Shark Head")
                    opponent_list.remove("Shark Head")
                    playing_opponents.append('Shark Head')


                elif chosen_player == '4':
                    print("You chose Will Turner")
                    opponent_list.remove("Will Turner")
                    playing_opponents.append('Will Turner')


                elif chosen_player == '5':
                    print("You chose Crab-Man")
                    opponent_list.remove("Crab-Man")
                    playing_opponents.append("Crab-Man")


                elif chosen_player == '6':
                    print("You chose Bootstrap Bill")
                    opponent_list.remove('Bootstrap Bill')
                    playing_opponents.append('Bootstrap Bill')

                else:
                    choose_player('4')


#Need to make a function to automatically remove chosen character from list,
# and add it to playing list.
#
#
#
#
#
#
#
#
#
#














def diceroll(playernumber,playerdice):
    for dice in playernumber:

        dice = (random.randint(1,6))
        playerdice.append(dice)

        print(dice)
        diceroll(player_1, player_1_dice)
        print(player_1_dice)


#roll dice for each player, random. range 1,6
# add numbers rolled to each players list

main()









