from math import sqrt

opt='y' # variable to store repeating condition

while((opt=='y')|(opt=='Y')):

	try:
		num = int(raw_input("\n\tEnter a number to check if it is prime = "))	
		if(num == 0):print "\n\t\"0\" is neither prime nor composite"
		else:
			num = abs(num) # If input is negative make it positive

			flag=0
			for i in range(2, int(sqrt(num))+1):
				if(num % i == 0):
					flag = 1
					break

			if(flag == 0): print "\t->", num, "is a PRIME number"
			else: print "\t->", num, "is NOT PRIME, it is divisible by ",i
			
	except ValueError: print "\n\t*** Invalid Input ***"

	opt=raw_input("\n\tDo you want to continue [Y/N] = ")
