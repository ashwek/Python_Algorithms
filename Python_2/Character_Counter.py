import os, sys # Importing Modules

opt='Y' # Variable to monitor recursion
while((opt=='y')|(opt=='Y')): # loop to continue program until asked to exit

        try:os.system("cls") # to clear WINDOWS terminal
        except:os.system("clear")  # to clear LINUX terminal

        print "\n\nThis program is made by \"ASHWEK\" to count the contents of a string \n" # Intro
        
        name=raw_input("Enter Anything below :\n=> ") # To take Input
        characters="aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789~!@#$%^&*()_+-=[]{}\\|;:\'\",<.>/?`" # List of characters that can be entered
        
        printed_characters=0 # for Formatted Output

        print "\nContents :\n"
        for check in range(0,(len(characters))): # Loop to check all characters from the list

                count=0 # Counting Variable

                for char in range(0,(len(name))): # Loop to go through every input character
                        if(name[char]==characters[check]):count+=1 # if there is a character increment the counter
                        
                if(count>0): # if the character exists Print it
                        printed_characters+=1
                        OutPut = str(characters[check]) + " = " + str(count) + ", "
                        sys.stdout.write(OutPut)
                        if((printed_characters%5)==0):print
                        
        opt=raw_input("\n\nDo you want to try again [Y/N] = ") # Ash User to continue or exit
