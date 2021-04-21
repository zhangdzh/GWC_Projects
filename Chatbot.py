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

responses=["That's cool!", "Wow. Riveting content.", "Great!", "Fantastic.", "Alright then.", "Okay.", "Nice story. Tell it again."]
def respond():
	chatting = True
	responseIndex=randint(0, len(responses)-1)
	print(responses[responseIndex])

def processInput(answer):
	if answer == "hello" or answer== "hey" or answer=="hi":
		print("Hi!")
	else:
		respond()

def randomquestions():
	RandQ=["How do you feel about sponges?", "What if I were an alien?", "Do you think robots should be capable of emotion?", "Are we all drifting aimlessly through space?", "Do you believe in the power of pineapples?", "Do you believe in the multiverse?", "What is the meaning of life?", "What should I pursue as a career outside of being stuck in a computer?"]
	qIndex=randint(0,len(RandQ)-1)
	print(RandQ[qIndex])
	input()
	RandA=["I don't know how I feel about that.", "You are kind of dead to me now.", "Oh...you're one of THOSE people...", "Are you a lizard?", "Me too. Me too.", "I didn't actually want an answer.", "Thanks! I don't care!", "I appreciate your input.", "Ok I'm tired now.", "Who told you to say that?"]
	aIndex=randint(0, len(RandA)-1)
	print(RandA[aIndex])
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
			print("Oh. Okay. I see how it is. Bye then.")
			chatting = False
			break
		processInput(answer)
		for x in range(randint(1,5)):
			randomquestions()
		print("Okay. This is a very important question.")
		print("Answer yes or no. Don't try to be fancy.")
		print(" ")
		print("Do you believe we should save the bananas?")
		fate=input()
		if fate=="yes" or fate=="Yes" or fate=="YES":
			print("Okay. Good. Congratulations. Now leave.")
			chatting=False
		else:
			print("SAVE!! THE!! BANANAS!! BEGONE.")
			chatting=False
			break


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
	main()
