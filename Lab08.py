import random

# Choices in a list
# 2-Scissors
# 1-Paper
# 0-Rock
choices = ["Rock", "Paper","Scissors"]

win_user = 0
win_comp = 0
tie = 0

while True:
   # Computer Choice - between choices
   computer_choice = random.choice([0,1,2])

   player_choice = int(input("Type 0 for Rock, 1 for Paper, 0 for Rock or other # for quit: "))
   
   if player_choice > 2:
   	break

   # Prints what user entered
   print("User entered : " + choices[player_choice])
   # Prints what computer entered
   print("Computer entered : " + choices[computer_choice])

   # Player1   S  P  R
   #           2  1  0
   #
   # Player2   P  R  S
   #           1  0  2
   # (P2+1)%3  2  1  0
   # So, if P1=P2, P1 win.

   if player_choice == computer_choice:
   	print('Tie!')
   elif (player_choice+1)%3 == computer_choice:
   	print("Computer won")
   else:
	   print("Player won")
