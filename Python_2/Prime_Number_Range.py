from sys import stdout
from math import sqrt

def Prime(Num):
	for x in range(2, int(sqrt(Num))+1):
		if(Num%x == 0):return False
	return True

try:
	Lower_Limit = int(raw_input("\n\t -> Enter the lower Limit = "))
	try:
		Upper_Limit = int(raw_input("\t -> Enter the upper limit = "))
		Lower_Limit = Lower_Limit if Lower_Limit > 0 else 1
		Upper_Limit = Upper_Limit if Upper_Limit > 0 else 1
		if(Upper_Limit < Lower_Limit): Lower_Limit, Upper_Limit = Upper_Limit, Lower_Limit
		Primes=0

		print "\nPrime numbers between ", Lower_Limit, " & ", Upper_Limit, " are : "

		for i in range(Lower_Limit,(Upper_Limit+1)):
			if(Prime(i)):
				stdout.write(str(i)+", ")
				Primes+=1
		print "\n\nThere are ", Primes, " prime numbeer between ", Lower_Limit, " & ", Upper_Limit
	except ValueError: print "\n\t***Invalid Upper Limit Input***\n"
except ValueError: print "\n\t***Invalid Lower Limit Input***\n"
