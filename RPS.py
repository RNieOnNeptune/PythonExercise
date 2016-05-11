#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
#compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game).

import random

def main():
	print "A new round of Rock-Paper-Scissors game starts, please enter 'r', 'p' or 's'."
	user = raw_input("Enter here: ")
	computer = random.choice(['r', 'p', 's'])
	compare(user, computer)
	ask()
	
def compare(user, computer):
	if user not in ['r', 'p', 's']:
		print "Invalid input."
	elif user == computer:
		print "Draw!"
	elif (user == 'r' and computer == 's') or \
	     (user == 'p' and computer == 'r') or \
		 (user == 's' and computer == 'p'):
		print "Congrats! You win!"
	else:
		print "You lose!"
		
def ask():
	print "Would you like to play again? Enter 1 for yes, enter 2 for no."
	x = raw_input("Enter here: ")
	if x not in ['1', '2']:
		print "Invalid input, I take it as a 'No'. Thank you!"
	elif int(x) == 1:
		main()
	else:
		print "Thank you!"
		
if __name__ == '__main__':
	main()	
	
