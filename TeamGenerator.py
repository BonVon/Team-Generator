# @author Matthew Herrick
# @date 2022-03-10
# @version 1.0
# Given a group of players, can create balanced teams of many players.

import random

class Team():
    def __init__(self):
        self.roster = []

def menu():
    print("***************")
    print("Team Generator")
    print("Select an Option")
    print("1. Generate balanced team")
    print("2. Generate unbalanced team")
    print("3. Select random person")
    print("4. Quit")
    print("***************")

def player_List():
    print("Enter the name or gamer tag of all players, separated by commas (Ex: Ninja, Pewdiepie, Jow Rogan)")
    playerList = input()
    playerList = playerList.split(",")
    print(playerList)
    playersPerTeam = len(playerList) / 2
    teamGenerator(playerList, playersPerTeam, 2)

def teamGenerator(playerList, playersPerTeam, numTeams):
    i = 0
    while i <= numTeams:
        emptyTeam = Team()
        for player in playerList:
            numbersTaken = []
            randomIndex = random.randint(1, playersPerTeam)
            if randomIndex not in numbersTaken:
                empty
        
            
    

def spotFinder(index, roster):
    index = random.randint(1,)
menu()
while True:
    option = int(input())
    if option == 1:
        player_List()
    elif option == 2:
        player_List()
    elif option == 3:
        player_List()
    elif option == 4:
        break