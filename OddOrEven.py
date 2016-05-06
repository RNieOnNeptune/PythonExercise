# Ask the user for two integer numbers, the first number named "num", the second number named "check". 
# Provide messages to the user regarding:
# 1. If "check" can be divided by 4, 2 or is an odd number.
# 2. If "check" can be divided evenly by "num".

def main():
	num, check = get_number()
	checkint = check_integer()
	divide2, divide4 = oddeven4(check)
	checknum = check_num(check, num)
	message(divide2, divide4, checknum)
	
def get_number():
	strlist = raw_input('Please input two numbers, separated by a comma: ').split(',')
	numlist = [int(strlist[0]), int(strlist[1])]
	return numlist
	
	
def oddeven4(check):
	divide2 = bool(check%2 == 0)
	if divide2 == True:
		divide4 = bool(check%4 == 0)
	else:
		divide4 = False
	return [divide2, divide4]
		
def check_num(check, num):
	return(bool(check%num == 0))
	
		
def message(divide2, divide4, checknum):
	if divide2 == True:
		if divide4 == True:
			print('The second number is a multiple of 4.')
		else:
			print('The second number is an even number, but not a multiple of 4.')
	else:
		print("The second number is an odd number.")
		
	if checknum == True:
		print('The second number can be divided evenly by the first number.')
	else:
		print('The second number cannot be divided evenly by the first number.')
		
		
if __name__ == '__main__':
	main()