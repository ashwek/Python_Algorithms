import sys

x='y' # Variable to store repeating condition

while((x=='y')|(x=='Y')): # loop to run program until asked to quit
        
        print "\n\n\nThis program is made by \"ASHWEK\" to find prime numbers within a range\n" # Intro
        
        try: # To handle Lower Limit Input errors
                Lower_Limit = int(input("\n\t -> Enter the lower Limit = "))
                
                try: # To handle Upper Limit Errors
                        Upper_Limit = int(input("\n\t -> Enter the upper limit = "))
                
                        if(Lower_Limit < 0 ):Lower_Limit = 1 # Set lower_limit as 1 if less than 1
                        if(Upper_Limit < Lower_Limit): # if Upper_limit is less than Lower_Limit, Swap them
                                temp = Upper_Limit
                                Upper_Limit = Lower_Limit
                                Lower_Limit = temp
                        if(Lower_Limit == 0):Lower_Limit = 1 # If lower_Limit is 0, make it 1

                        Primes=0 # number of prime numbers between the limit
                
                        print "\nPrime numbers between ", Lower_Limit, " & ", Upper_Limit, " are :\n"

                        for i in range(Lower_Limit,(Upper_Limit+1)): # Loop to find prime numbers between the range
                                flag=0
                                for j in range(2,i):
                                        if(i%j==0):
                                                flag=1
                                                break
                                if(flag==0):
                                        sys.stdout.write(str(i)+", ") # if it is a prime number, print it
                                        Primes+=1 # Number of Prime numbers
                        
                        print "\n\nThere are ", Primes, " prime numbeer between ", Lower_Limit, " & ", Upper_Limit
                except NameError: print "\n\n***Invalid Lower Limit Input***"
        except NameError: print "\n\n***Invalid Upper Limit Input***"

        x=raw_input("\n\nDo you want to try another range [Y/N] = ") # Asks user to continue of exit
