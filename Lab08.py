while True:
	x = int(input("type 2-4 to # of players or other # to finish: "))
	if x == 0 or x < 2 or x > 4:
		break
	players = []
	for y in range(x):
		players.append(int(input("Player "+str(x)+", choose 1 for Rock 2 for Scissors 3 for Paper: ")))
		x -= 1
	print("Player #"+str(players.index(max(players))+1)+" is the winer.")
