x = input("Type a name: ")
x = x.upper()

if x == x[::-1]:
	print("It is a palindrome")
else:
	print("It is not a palindrome")
