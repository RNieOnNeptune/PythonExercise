#Ask the user for a number and determine whether the number is prime or not. 
#(For those who have forgotten, a prime number is a number that has no divisors.). 
#You can (and should!) use your answer to [Exercise 4]

def main():
	num1 = check()
	prime1, divisor1 = is_prime(num1)
	printprime(prime1, divisor1)
	
	
def check():
	while True:
		try:
			x = int(raw_input("Please enter an integer number: "))
			if x > 0:
				return x
			else: 
				print "This number is not positive, please try again."
		except ValueError:
			print "This is not an integer number, please try again."
			
def is_prime(num):
	divisor = 0
	if num == 1:
		prime = False
	elif num == 2:
		prime = True
	else:
		prime = True
		for k in range(2, (num/2+1)):
			if num%k == 0:
				divisor = k
				prime = False
				break
	return [prime, divisor]
	
def printprime(prime, divisor):
	if prime:
		print "This is a prime!"
	else:
		print "This is not a prime. One of the divisor is: {}".format(divisor)
		
	
if __name__ == '__main__':
	main()
	

	
