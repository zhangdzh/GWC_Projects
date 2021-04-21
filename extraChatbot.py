# --- Define your functions below! ---
from random import *

def intro():
	chatting=True
	print("Hi! Nice to meet me. I know. Thanks.")
	print("What's your name?")
	name=input()
	print(name, "is a nice name.")
	chatting = False
def lifequestions():
	chatting = True
	print("On a scale of 1-10 how would you rate your life at the moment?")
	life=input()
	print("Wow. A", life, ". How relatable.")
	chatting = False

def animal():
	chatting=True
	print("What are your favorite animals?")
	animal1=input()
	print("Cool. I like tigers, but", animal1, "are cool too.")

responses=["That's cool!", "Wow. Riveting content.", "Alright then.", "I hear the bananas speaking through you.", "Okay.", "Nice story. Tell it again."]
def respond():
	chatting = True
	responseIndex=randint(0, len(responses)-1)
	print(responses[responseIndex])

def processInput(answer):
	if answer == "hello" or answer== "hey" or answer=="hi":
		print("Hi!")
	else:
		if answer == "number":
			print("Ok")
		if answer == "menu":
			print("Ok")
		else:
			respond()
			print("You can also say 'number' to play Guess the Number and 'menu' for a random menu")

def numbergame():
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

def menugame():
	entrees=["burger", "chicken", "steak", "pasta"]
	sides=["macaroni and cheese", "salad", "fries", "biscuit", "coleslaw", "fruit"]
	desserts=["sundae", "cheesecake", "strawberry shortcake", "pie"]
	drinks=["soda", "smoothie", "milkshake", "water"]

	print("Here's your random menu:")

	EntreeIndex=randint(0, len(entrees)-1)
	SidesIndex=randint(0, len(sides)-1)
	SidesIndex2=randint(0, len(sides)-1)
	DessertIndex=randint(0, len(desserts)-1)
	DrinkIndex=randint(0, len(drinks)-1)

	print("Your entree is", entrees[EntreeIndex])
	print("Your sides are", sides[SidesIndex], "and", sides[SidesIndex2])
	print("Your dessert is", desserts[DessertIndex])
	print("Your drink is", drinks[DrinkIndex])

	dessertprice=randint(3,7)
	entreeprice=randint(7,12)
	sidesprice=randint(3,6)
	sidesprice2=randint(2,5)
	drinkprice=randint(1,3)

	print("Your total cost is", entreeprice+sidesprice+dessertprice+sidesprice2+drinkprice, "dollars")

# --- Put your main program below! ---
def main():
	chatting = True
	intro()
	lifequestions()
	animal()
	while chatting:
		# --- Call your functions below! ---

		answer = input("(What will you say?) ")

		if answer == "done":
			print("Wow okay bye then")
			chatting = False
			break
		processInput(answer)
		#print("Say 'number' to play Guess the Number and 'menu' for a random menu")
		if answer == "number":
			numbergame()
		if answer == "menu":
			menugame()
		'''if answer == "hello" or answer== "hey" or answer=="hi":
			print("Hi!")
		else:
			respond()'''

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
	main()
