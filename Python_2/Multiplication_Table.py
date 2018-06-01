"""

Multiplication Table

"""

opt='y' # Variable to store Repeating Condition

while((opt=='y')|(opt=='Y')): # To run the program till asked to exit
        
        print "\n\nThis program is written by \"ASHWEK\" to print tables" # Intro
        
        try: # to handle Number Input error
                num=float(input("\n\tEnter a number = ")) # To input a number
                
                try: # To handle limit Input error
                        limit=int(input("\tEnter a limit = ")) # Limit Input
                        
                        print 

                        for n in range (1,limit+1): # Loop to print the Tables
                                print "\t -> ",num,"*",n,"=",(num*n)
                                
                        opt=raw_input("\nDo you want to continue [Y/N] = ") # To give chooice to continue or not
                        
                except NameError: print "*** Invalid Limit Entered ***"
        except NameError: print "*** Invalid Number Entered ***"
