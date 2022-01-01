import random

while True:
	computer = random.randint(1, 9)
	guess = input("Type a integer number between 1 and 9 or exit to quit: ")
	if guess.lower() == "exit":
		break
	player = int(guess)
	guesses = 1
	while player != computer:
		if player < computer:
			print("it is low. try again.")
		else:
			print("it is high. try again.")
		guesses += 1
		player = int(input("Type other integer number between 1 and 9: "))
	print("###You tried "+str(guesses)+" time(s)###")
print("See you soon!")
