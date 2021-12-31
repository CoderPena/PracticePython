while True:
	x = int(input("type 2-4 to # of players or other # to finish: "))
	if x == 0 or x < 2 or x > 4:
		break
	players = []
	for y in range(x):
		players.append(int(input("Player "+str(x)+", choose 1 for Rock 2 for Scissors 3 for Paper: ")))
		x -= 1
	print("Player #"+str(players.index(max(players))+1)+" is the winer.")





import random
import sys

# Choices in a list
# 2-Scissors
# 1-Paper
# 0-Rock
choices = ["Rock", "Paper", "Scissors"]

win_user = 0
win_comp = 0
tie = 0

# Computer Choice - between choices
computer_choice = random.choice(choices)

player_choice = int(input("choose: 0 for Rock, 1 for Paper, 2 for Scissors or other # for quit: "))



# Prints what user entered
print("User entered : " + str(player_choice))
# Prints what computer entered
print("Computer entered : " + str(computer_choice))

