'''
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence 
is the sum of the previous two numbers in the sequence. 
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, ...
'''

def main():
	n = int(raw_input("Enter a number: "))
	print fibo(n)
	
def fibo(n):
	if n == 1:
		l = [1]
	elif n == 2:
		l = [1, 1]
	else:
		l = [1, 1]
		for i in range(2, n):
			l.append(l[-1]+l[-2])
	return l
	
if __name__ == '__main__':
	main()
