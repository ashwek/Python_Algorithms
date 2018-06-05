from sys import exit

choice=0
while(choice!=3):

	print "\n\t1. Celsius-to-Fahrenheit"
	print "\t2. Fahrenheit-to-Celsius"
	print "\t3. EXIT"
	try: choice=int(raw_input("Enter your option = "))
	except: choice=0
	
	x=0.0
	
	if(choice == 1): # for C-F
		try:
			c=float(raw_input("\n\tEnter temp. in C = "))
			print "\tTemp. in Fahrenheit = ", (c*9/5)+32
		except ValueError: print "\n***Invalid Input***"
	elif(choice == 2): # for F-C
		try:
			f=float(raw_input("\n\tEnter temp. in F = "))
			print "\tTemp. in Celsius = ", (5*(f-32))/9
		except ValueError: print "\n***Invalid Input***"
	elif(choice==3): exit()
	else: print "\n***Invalid Input***"
	
	raw_input("\nPress ENTER to continue...")
