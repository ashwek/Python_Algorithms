import sys, os # Importing Modules

choice=0 # Loop controling variable
while(choice!=3): # Loop to repeat the program until asked to exit
        
	try : os.system("cls") # To clear WINDOWS terminal
	except : os.system("clear") # To clear LINUX terminal

	print "\n\nThis program is made by \"ASHWEK\" to convert Celsius-to-Fahrenheit & Fahrenheit-to-Celsius\n\n" # Intro
	print "\t1. Celsius-to-Fahrenheit"
	print "\t2. Fahrenheit-to-Celsius"
	print "\t3. EXIT"
	try: choice=int(input("Enter your option = ")) # Choice Input
	except: choice=0 # If choice is invalid make it 0
	
	x=0.0
	
	if(choice == 1): # for C-F
		try: # handling invalid Input
			c=float(input("\n\nEnter temp. in C to convert into F = ")) # input temp in C
			x=(c*9/5)+32 # convert C to F
			print "\n\tTemp. in Celsius = ",c # OUTPUT
			print "\tTemp. in Fahrenheit = ",x
		except: print "\n***Invalid Input***" # message for invalid input
	elif(choice == 2): # for F-C
		try: # to handle invalid Input
			f=float(input("\n\nEnter temp. in F to convert into C = ")) # input temp in f
			x=(5*(f-32))/9 # Convert F to C
			print "\n\tTemp. in Fahrenheit = ",f # Output
			print "\tTemp. in Celsius = ",x
		except: print "\n***Invalid Input***" # message for invalid input
	elif(choice==3): # exit program option
		print "\n\t***Program Successfullt Terminatd***"
		sys.exit() # exit program
	else: print "\n***Invalid Input***"
	
	raw_input("\nPress ENTER to continue...") # Buffer stop
