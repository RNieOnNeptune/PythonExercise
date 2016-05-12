#Generate a random number between 1 and 9 (including 1 and 9). 
#Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
#Extras:
#Keep the game going until the user types 'exit'
#Keep track of how many guesses the user has taken, and when the game ends, print this out.


import random

def main():
	num_generate = random.randint(1, 9)
	print 'You have made {} guesses.'.format(guess(num_generate))
	
def guess(num_generate):
	i = 0
	print "Type 'exit' to quit."
	num_guess = raw_input("Please guess the number generated (between 1 and 9): ")
	while num_guess != 'exit':
		i = i + 1
		guess = int(num_guess)
		if guess == num_generate:
			print "You are right!"
			break
		else:
			if guess > num_generate:
				print "Your guess is too high."
			else: 
				print "Your guess is too low."
			num_guess = raw_input("Please guess the number generated (between 1 and 9): ")
	return i 
	
if __name__ == '__main__':
	main()
