from Player import *

# List to contain the players in a basketball team
basketball_team = []
basket_name = input("Enter the basketball team name: ")

for i in range(5):
    name = input("Enter player name: ")
    player = BasketBallPlayer(name)
    position = input("Which position is he/she playing? ")
    player.set_position(position)
    # Add the player to the basketball team
    basketball_team.append(player)

print(f"Team {basket_name} consists of the following players: ")

for player in basketball_team:
    print(player)
