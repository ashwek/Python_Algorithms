import sys

opt='y' # Variable to store repeating condition
while((opt=='y')|(opt=='Y')): # Loop to continue program until asked to exit

        print "\n\nThis program is made by \"ASHWEK\" to find prime factors of any number \n\n" # Intro
        
        try: # To handle Number Input Error
                num = int(input("Enter a number to find its prime factors = ")) # Input Number

                if(num < 0 ): num = -num # If input number is -ve make it +ve
                
                x=num # Making temporary copy to protect orignal data
                flag=total=0 

                sys.stdout.write("\n -> Factors are : ")
        
                while(x!=1): # To run program until all Factors are calculated
                        flag = 0
                        for i in range(2, x):
                                if(x % i == 0):
                                        sys.stdout.write(str(i) + ",")
                                        x = x / i
                                        total+=1
                                        flag = 1
                                        break
                        if(flag == 0):
                                sys.stdout.write(str(x))
                                total+=1
                                x=1
                                
                print "\n\nThere are ", total, " factors of ", num # Print final details
        except NameError: print"\n*** Invalid Input ***"
        opt=raw_input("\n\nDo you want to cintinue [Y/N] = ") # To ask user to continue or exit
