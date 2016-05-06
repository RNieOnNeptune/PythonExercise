#Create a program that asks the user for a positive integer and then prints out a list of all the divisors of that number.

num = int(raw_input("Please input a positive integer: "))
divisorlist = [i for i in range(1, num+1) if num % i == 0]
print divisorlist
