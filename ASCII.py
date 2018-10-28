from os import system
from sys import exit
choice=0 # variable to contol program termination

while(choice!=3): #loop to continue program until asked to exit
	system("clear") #Clear Screen for Linux Terminal
	#system("cls") #Clear Screen for Windows
	
	print "\n\nFind ASCII value of a character"
	print "\t1. Number to Character" 
	print "\t2. Character to Number" 
	print "\t3. EXIT" 
	
	try : choice=int(input("Enter your choice = "))
	except : choice=0

	if(choice==1):
		try:
			num=int(input("\nEnter a NUMBER to find its corresponding character  = "))
			print '\n ->', num, 'is the ASCII value for', chr(num) 
		except: print "\n***Invalid Input***"
	elif(choice==2):
		try:
			char=ord(raw_input("\nEnter a character to find its ASCII value = "))
			print "\n -> ASCII value of", chr(char), "is", char 
		except: print "\n***Invalid Input***"
	elif(choice==3): exit()
	else:print "\n***Invalid Input***"
	
	raw_input("\nPress ENTER to continue...")
