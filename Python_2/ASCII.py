import os, sys # importing modules

choice=0 # variable to contol program termination
while(choice!=3): # loop to continue program until asked to exit
	try:os.system("cls") # clear WINDOWS terminal
	except:os.system("clear") # clear LINUX Terminal

	print "\n\nThis program is made by \"ASHWEK\" to find ASCII value of a character\n" # Intro 
	print "\t1. Number to Character" 
	print "\t2. Character to Number" 
	print "\t3. EXIT" 
	
	try : choice=int(input("Enter your choice = ")) # input Option
	except : choice=0 # if input is invalid

	if(choice==1): # if N-C
		try: # to handle invalid input
			num=int(input("\nEnter a number to find its corresponding character  = ")) # to input a Number
			char=chr(num) # converting to character
			print '\n',num,' is the ASCII value for ',char # printing result 
		except: print "\n\n***Invalid Input***"  # message for invalid input
	elif(choice==2): # if C-N
		try: # to handle invalid input
			char=raw_input("\n\nEnter a character to find its ASCII value = ") # to input character
			num=ord(char) # converting to ASCII value
			print "\nASCII value of ",char," is ",num # printing result 
		except: print "\n\n***Invalid Input***" # message if input is invalid
	elif(choice==3): # exit option
		print "\n\n\t***Program Successfully Terminated***" 
		sys.exit() # Exit program
	else:print "\n\n***Invalid Input***" # if invalid Option
	
	raw_input("\n\nPress ENTER to continue...")
