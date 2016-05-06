#Take two lists, say for example these two:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
#Make sure your program works on two lists of different sizes.
#Extras:
#Randomly generate two lists to test this
#Write this in one line of Python 

import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
m = 20
l = 20

def main():
	print 'The overlap list of a and b is: {}'.format(findcommon())
	list1 = lgenerator()
	list2 = lgenerator()
	print 'The overlap list of the two random lists is: {}'.format(findcommon(l1 = list1, l2 = list2))
	
# I restrict the largest number in the random list to be 'm',
# the maximum length of the list to be 'l'.	
def lgenerator(maxlen = l, maxnum = m):
	len = random.randrange(maxlen)
	thelist = []
	for i in range(0, len):
		thelist.append(random.randrange(maxnum))
	print 'The random list is: {}'.format(thelist)
	return thelist

# Since I use set here, the common elements I find are unique ones, duplicates are removed.
def findcommon(l1 = a, l2 = b):
	return list(set(l1)&set(l2))
	
if __name__ == '__main__':
	main()
	
	
	
	
	
