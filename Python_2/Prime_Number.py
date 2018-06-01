opt='y' # variable to store repeating condition

while((opt=='y')|(opt=='Y')): # Loop to run program until asked to exit
        
	print "\n\nThis program is made by \"ASHWEK\" to check if a number is prime or not \n" # Intro
	
	try: # To handle Input Number Errors 
		num = int(input("\t -> Enter a number to check if it is prime = ")) # To take input
	
		if(num == 0):print "\n\t\"0\" is neither prime nor composite"
		else:
			if(num<0): num = -num # If input is negative make it positive

			flag=0
			for i in range(2, num): # Pinding if it is prime or not
				if(num % i == 0):
					flag = 1
					break

			if(flag == 0): print "\n\t", num, " is a PRIME number"
			else: print "\n\t", num, " is NOT PRIME, it is divisible by ",i
			
	except NameError: print "\n*** Invalid Input ***"

	opt=raw_input("\n\nDo you want to continue [Y/N] = ") # to ask user to continue or exit
