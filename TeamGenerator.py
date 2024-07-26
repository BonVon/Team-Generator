# @author Matthew Herrick
# @date 2022-03-10
# @version 1.0
# Given a group of players, can create balanced teams of many players.

import random

def menu():
    print("***************")
    print("Team Generator")
    print("Select an Option")
    print("1. Generate balanced team")
    print("2. Generate unbalanced team")
    print("3. Select random person")
    print("4. Quit")
    print("***************")

def list_cleaner():
    playerList = input("Enter the name or gamer tag of all players, separated by commas (Ex: Ninja, Pewdiepie, Jow Rogan)")
    playerList = playerList.split(",")
    playerList = [name.strip() for name in playerList]
    return playerList

def balanced_teams_generator():
    playerList = list_cleaner()
    playersPerTeam = len(playerList) / 2
    teams_generator(playerList, 2, playersPerTeam)

def unbalnced_teams_generator():
    numTeams = input("How many teams will there be?\n")
    if numTeams % 2 == 0:
        print("You idiot, thats an even number of teams.")
        balanced_teams_generator()
    playerList = list_cleaner()
    teams_generator(playerList, numTeams)


def random_player():
    playerList = list_cleaner()
    randomIndex = random.randint(0, len(playerList))
    print(f"Chosen Player: {playerList[randomIndex]}")

def teams_generator(playerList, numTeams, playersPerTeam = None):
    shuffledTeam = random.shuffle(playerList)
    if numTeams == 2:
        teamOne = shuffledTeam[:int(playersPerTeam)]
        teamTwo = shuffledTeam[int(playersPerTeam):]
        print(f"\nYour two teams:\nTeam 1: {teamOne}\nTeam 2: {teamTwo}\n")
        return

while True:
    menu()
    option = int(input())
    if option == 1:
        balanced_teams_generator()
    elif option == 2:
        unbalnced_teams_generator()
    elif option == 3:
        random_player()
    elif option == 4:
        exit()


