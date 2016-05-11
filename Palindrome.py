#Ask the user for a string and print out whether this string is a palindrome or not. 
#(A palindrome is a string that reads the same forwards and backwards.)

# Assume the letters have the same cases, otherwise use str.lower()

def main():
	str = raw_input('Please input a string: ')
	print 'Is the string a palindrome? {}'.format(palin2(str))

# Method 1: Compare the first half with the second half
def palin1(str):
	x = False
	for i in range(0, (len(str)//2 + 1)):
		if str[i] != str[-(i+1)]:
			break
	else:
		x = True
	return x
	
# Method 2: reverse the string
def palin2(str):
	x = False
	str_reverse = str[::-1]
	if str == str_reverse:
		x = True
	return x
	
if __name__ == '__main__':
	main()
