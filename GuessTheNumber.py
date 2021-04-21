#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)
tries=0
while tries<3:
	guess = input("Guess a number between 1 and 20 (inclusive): ")
	tries+=1
	if not guess.isnumeric(): # checks if a string is only digits 0 to 9
		print("That's not a positive whole number, try again!")
	else:
		guess = int(guess) # converts a string to an integer
		if guess<1 or guess>20:
			print("I SAID PICK A NUMBER BETWEEN 1 AND 20")
		else:
			if guess>aRandomNumber:
				print("Guess lower")
			else:
				if guess<aRandomNumber:
					print("Guess higher")
				else:
					print("Congratulations")
					break
print("The number was", aRandomNumber)
