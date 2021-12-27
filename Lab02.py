nNum = int(input("Type a integer number:"))
nCheck = int(input("Type a integer check number:"))

if nNum % 2 == 0:
	print("Even number")
else:
	print("Odd number")
	
if nNum % nCheck == 0:
	print(str(nNum) + " is divisible by " + str(nCheck))
else:
	print(str(nNum) + " is not divisible by " + str(nCheck))
	
